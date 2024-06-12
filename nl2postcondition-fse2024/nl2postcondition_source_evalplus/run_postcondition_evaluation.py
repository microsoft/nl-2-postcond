import argparse
import json
import multiprocessing
import os
import pickle
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union
import sys
import log
import glob
import shutil


import numpy as np
from tqdm import tqdm

from evalplus.data import (
    CACHE_DIR,
    get_human_eval_plus,
    get_human_eval_plus_hash,
    load_solutions,
)
from evalplus.eval import (
    SUCCESS,
    compatible_eval_result,
    estimate_pass_at_k,
    untrusted_check,
    untrusted_postcondition_check,
)
from evalplus.gen.util import trusted_exec

from response_preprocessing import code_sanitize, wrap_code_solution
# 1st item: the status
# 2nd item (optional): the detailed pass/fail boolean for each input
Result = Tuple[str, List[bool]]

def get_groundtruth(problems, hashcode):
    cache_file = os.path.join(CACHE_DIR, f"{hashcode}.pkl")
    if os.path.exists(cache_file):
        print(f"Load from {cache_file}")
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    print("Computing expected output...")
    tbegin = time.time()
    expected_output = {}
    for task_id, problem in problems.items():
        #print(task_id, len(problem["base_input"]), len(problem["plus_input"]))
        #print(problem['plus_input'])
        oracle = {}
        oracle["base"], oracle["base_time"] = trusted_exec(
            problem["prompt"] + problem["canonical_solution"],
            problem["base_input"],
            problem["entry_point"],
            record_time=True,
        )

        oracle["plus"], oracle["plus_time"] = trusted_exec(
            problem["prompt"] + problem["canonical_solution"],
            problem["plus_input"],
            problem["entry_point"],
            record_time=True,
        )
        expected_output[task_id] = oracle
    print(f"Expected outputs computed in {time.time() - tbegin:.2f}s")

    with open(cache_file, "wb") as f:
        pickle.dump(expected_output, f)
    import sys
    sys.set_int_max_str_digits(0)
    #json.dump(expected_output, open(f"/app/expected_output.json", "w"))
    return expected_output

def check_correctness(
    completion_id: int,
    problem: Dict[str, Any],
    solutionDict: Dict[Any, Any],
    expected_output: Dict[str, List],
    base_only=False,
    fast_check=False,
    identifier=None,
    min_time_limit: float = 0.1,
    gt_time_limit_factor: float = 2.0,
) -> Dict[str, Union[int, Optional[Result]]]:
    if solutionDict["is_duplicate"] is None:
        isdupe = False
    elif solutionDict["is_duplicate"]["SyntaxMatch"] is None:
        isdupe = False
    else:
        isdupe = True
    all_time_limits = expected_output["base_time"] + expected_output["plus_time"]
    ret = {
        "completion_id": completion_id,
        "task_id": problem["task_id"],
        "_identifier": identifier,
        "llm_response_num": solutionDict["response_num"],
        "compiles": solutionDict["compiles"],
        "is_syntax_dupe": isdupe,
        "postcondition_alone": solutionDict["postcondition_alone"],
        "entry_point": solutionDict["entry_point"],
        "time_limits": all_time_limits,

    }
    ret["base"] = untrusted_check(
        solutionDict["solution"],
        problem["base_input"],
        problem["entry_point"],
        expected=expected_output["base"],
        atol=problem["atol"],
        ref_time=expected_output["base_time"],
        fast_check=fast_check,
        min_time_limit=min_time_limit,
        gt_time_limit_factor=gt_time_limit_factor,
    )

    if not base_only:
        ret["plus"] = untrusted_check(
            solutionDict["solution"],
            problem["plus_input"],
            problem["entry_point"],
            expected=expected_output["plus"],
            atol=problem["atol"],
            ref_time=expected_output["plus_time"],
            fast_check=fast_check,
            min_time_limit=min_time_limit,
            gt_time_limit_factor=gt_time_limit_factor,
        )

    return ret

def check_postcondition_kills(
    completion_id: int,
    sample: Dict[str, Any],
    entry_point: str,
    postcondition_response_num: int,
    postcondition_all_time_limits : List[float],
    min_time_limit: float = 0.1,
    gt_time_limit_factor: float = 2.0
) -> Dict[str, Union[int, Optional[Result]]]: 
    ref_times = [postcondition_all_time_limits[i] for i in sample['unique_bopi_id'] if i < len(postcondition_all_time_limits)]

    ret = {
        "completion_id": completion_id,
        "task_id": sample["task_id"],
        "_identifier": sample['_identifier'],
        "buggy_code_response_num": sample["response_num"],
        "post_condition_response_num": postcondition_response_num,
    }
    ret["test_results"] = untrusted_postcondition_check(
        sample["wrapped"], # The wrapped code
        sample['unique_bopi'], # The unique buggy inputs
        entry_point, # the function entry point
        ref_times, # The timelimits for the unique buggy
        min_time_limit=min_time_limit,
        gt_time_limit_factor=gt_time_limit_factor,
    )
    
    return ret

def evaluate_post_condition_power(wrapped_codes, postcondition_info, n_workers, flags, print_and_log):
    """
    This function evaluates the soundness of the post-conditions in the sample file.
    If the flag --cashed is true, then will just load the results from a cashed file.
    Otherwise, it will run the evaluation and save the results to a cashed file
    """
    # If we get here, we are doing the evaluation
    result_path = os.path.join(log.OUTPUT_FOLDER, log.SUB_FOLDER, '{}'.format(postcondition_info['task_id'].replace('/', '_')), 'postcondition_{}.json'.format(postcondition_info['response_num']))
    if os.path.isfile(result_path) and not flags.i_just_wanna_run:
        print_and_log("😍 Found existing power run at {}!!\n\tLoading and moving on...".format(result_path))

        print_and_log(f"Load from {result_path}")
        with open(result_path, "r") as f:
            this_power_result = json.load(f)

        return this_power_result

    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = []
        completion_id = Counter()
        n_samples = 0
        eval_results = defaultdict(list)
        remainings = set()

        print("Reading samples...")
        for sample in tqdm(wrapped_codes):
            task_id = sample["task_id"]
            sample["_identifier"] = sample["response_num"]
            entry_point = postcondition_info['entry_point']
            remainings.add(sample["_identifier"])
            args = (
                completion_id[task_id],
                sample,
                entry_point,
                postcondition_info['response_num'],
                postcondition_info['all_time_limits'],
                flags.min_time_limit,
                flags.gt_time_limit_factor,
            )
            futures.append(executor.submit(check_postcondition_kills, *args))
            completion_id[task_id] += 1
            n_samples += 1

        assert n_samples == len(remainings), "Missing problems in unfinished"
        assert len(completion_id) == 1, "Should only give one problem for this one"

        def stucking_checker():
            while remainings:
                last_size = len(remainings)
                time.sleep(10)
                if last_size == len(remainings) and len(remainings) > 0:
                    print(f"Stucking for 10 seconds... {len(remainings)} left")
                    
                    print("First five remaining:")
                    for remaining in list(remainings)[:5]:
                        print(remaining)
                        #pass
                        
        threading.Thread(target=stucking_checker).start()

        for future in tqdm(as_completed(futures), total=n_samples):
            result = future.result()
            remainings.remove(result["_identifier"])
            eval_results[result["task_id"]].append(result)

    # sort the results for each problem by completion_id
    power_results = {}
    for task_id, task_results in eval_results.items():
        task_results.sort(key=lambda x: x["completion_id"])
        power_results[task_id] = {
            "nbuggyPrograms": len(task_results),
            "buggy_code_response_num": [x["buggy_code_response_num"] for x in task_results],
            "post_condition_response_num": [x["post_condition_response_num"] for x in task_results],
            "num_tests_run": sum(len(x["test_results"][1]) for x in task_results),
            "num_tests_killed": sum(sum(x["test_results"][1]) for x in task_results),
            "test_results": [x["test_results"] for x in task_results],
            
        }



    if os.path.isfile(result_path) and flags.i_just_wanna_run:
        decision = ""
        while decision.lower() not in ["y", "n"]:
            print(f"{result_path} already exists. Press [Y/N] to overwrite or exit...")
            decision = input()

        if decision.lower() == "y":
            # mv the file to a backup
            new_path = result_path + ".bak"
            while os.path.isfile(new_path):
                new_path += ".bak"
            os.rename(result_path, new_path)
            print(f"Backup {result_path} to {new_path}")

    if not os.path.isfile(result_path):
        base_path = "/".join(result_path.split("/")[:-1])
        if not os.path.exists(base_path):
            try:
                os.makedirs(base_path)
            except:
                print_and_log("Failed to make dir")
                
        with open(result_path, "w") as f:
            json.dump(power_results, f)

    
    
    with open(result_path, "w") as f:
        json.dump(power_results, f)
    
    return power_results

def evaluate_post_condition_soundness(flags, n_workers, postcondition_sample_dir, print_and_log, log_only, problems):
    """
    This function evaluates the soundness of the post-conditions in the sample file.
    If the flag --cashed is true, then will just load the results from a cashed file.
    Otherwise, it will run the evaluation and save the results to a cashed file
    """
    # If we get here, we are doing the evaluation
    
    print_and_log("Trying to load preprocessed samples... ")
    # Load the raw data in from the samples_partial llmGen jsonl file
    preprocessedSamplesFile = glob.glob(os.path.join(postcondition_sample_dir, 'preprocessed_samples*'))
    
    if not preprocessedSamplesFile:
        print_and_log("⚠️  Warning: No readable jsonl file in {}, aborting folder".format(postcondition_sample_dir))
        return
    elif len(preprocessedSamplesFile) > 1:
        print_and_log("⚠️  Warning: More than one readable jsonl file {}, aborting folder".format(postcondition_sample_dir))
        return
    
    assert len(preprocessedSamplesFile) == 1
    print_and_log("😊  Successfully located the preprocessed samples at".format(len(postcondition_sample_dir)))

        
    # This is if the soundness evaluation has already been run -> we can just load the results
    result_path = os.path.join(log.OUTPUT_FOLDER, "soundness_eval_results_" + preprocessedSamplesFile[0].split('/')[-1])
    if os.path.isfile(result_path) and not flags.i_just_wanna_run:
        print_and_log("😍 Found existing soundness run at {}!!\n\tLoading and moving on...".format(result_path))

        print(f"Load from {result_path}")
        with open(result_path, "r") as f:
            soundness_results = json.load(f)

        soundness_results = compatible_eval_result(soundness_results)

    # Otherwise, we need to run the evaluation
    else:
        # Check that there is actually one sample file that matches

        
        # Copy over the config and raw file and the like from the raw folder
        print_and_log("Now copying raw llm samples and generation meta data... ")
        oldHydra = os.path.join(postcondition_sample_dir, 'llmGenConfig_HydraCopy')
        oldHydraCopy = os.path.join(log.OUTPUT_FOLDER, 'llmGenConfig_HydraCopy')
        shutil.copytree(oldHydra, oldHydraCopy, dirs_exist_ok=True)
        print_and_log("😊  Successfully copied llm gen hydra from: {} problems".format(oldHydra))
        shutil.copy(preprocessedSamplesFile[0], os.path.join(log.OUTPUT_FOLDER, 'raw_preprocessed_samples.jsonl'))
        print_and_log("😊  Successfully copied raw preprocessed samples as reference!!")
    
        print_and_log("⚒️  Now, calculating the ground truth...")

        #problems = get_human_eval_plus(mini=flags.mini)
        dataset_hash = get_human_eval_plus_hash()
        expected_output = get_groundtruth(problems, dataset_hash)
        
        print_and_log("😊  Humaneval plus and ground truth loaded!! 😊")

        soundness_results = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "hash": dataset_hash,
            "eval": {},
        }
        
        print_and_log("⚒️  Conducting soundness evaluation...")

        useBaseHumanEvalOnly = False

        if flags.base_only or flags.dataset == "humanevalbase":
            useBaseHumanEvalOnly = True 

        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            futures = []
            completion_id = Counter()
            n_samples = 0
            eval_results = defaultdict(list)
            remainings = set()

            print_and_log("Reading samples...")
            for sample in tqdm(load_solutions(preprocessedSamplesFile[0])):
                task_id = sample["task_id"]
                solution = (
                    sample["solution"]
                    if "solution" in sample
                    else problems[task_id]["prompt"] + sample["completion"]
                )
                sample["solution"] = solution
                remainings.add(sample["_identifier"] + '_llmResponseNum_' + str(sample["response_num"]))
                args = (
                    completion_id[task_id],
                    problems[task_id],
                    sample,
                    expected_output[task_id],
                    useBaseHumanEvalOnly,
                    not flags.test_details,  # fast_check
                    sample["_identifier"],
                    flags.min_time_limit,
                    flags.gt_time_limit_factor,
                )
                futures.append(executor.submit(check_correctness, *args))
                completion_id[task_id] += 1
                n_samples += 1

            assert n_samples == len(remainings), "Missing problems in unfinished"
            assert len(completion_id) == len(problems), "Missing problems in samples"

            def stucking_checker():
                while remainings:
                    last_size = len(remainings)
                    time.sleep(10)
                    if last_size == len(remainings) and len(remainings) > 0:
                        print(f"Stucking for 10 seconds... {len(remainings)} left")
                        
                        print("First five remaining:")
                        for remaining in list(remainings)[:5]:
                            print(remaining)
                            #pass
                            

            threading.Thread(target=stucking_checker).start()

            for future in tqdm(as_completed(futures), total=n_samples):
                result = future.result()
                remainings.remove(result["_identifier"] + '_llmResponseNum_' + str(result["llm_response_num"]))
                eval_results[result["task_id"]].append(result)

        # sort the results for each problem by completion_id
        for task_id, task_results in eval_results.items():
            task_results.sort(key=lambda x: x["completion_id"])
            soundness_results["eval"][task_id] = {
                "nfiles": len(task_results),
                "entry_point": [x["entry_point"] for x in task_results],
                "llm_response_num": [x["llm_response_num"] for x in task_results],
                "compiles": [x["compiles"] for x in task_results],
                "is_syntax_dupe": [x["is_syntax_dupe"] for x in task_results],
                "postcondition_alone": [x["postcondition_alone"] for x in task_results],
                "base": [x["base"] for x in task_results],
                "plus": [x["plus"] for x in task_results]
                if not useBaseHumanEvalOnly
                else [],
                "ref_time": task_results[0]["time_limits"],
            }

    print_and_log("😊  Finished running evaluation -> now time to save the results 😊")

    if os.path.isfile(result_path) and flags.i_just_wanna_run:
        decision = ""
        while decision.lower() not in ["y", "n"]:
            print(f"{result_path} already exists. Press [Y/N] to overwrite or exit...")
            decision = input()

        if decision.lower() == "y":
            # mv the file to a backup
            new_path = result_path + ".bak"
            while os.path.isfile(new_path):
                new_path += ".bak"
            os.rename(result_path, new_path)
            print(f"Backup {result_path} to {new_path}")

    if not os.path.isfile(result_path):
        with open(result_path, "w") as f:
            json.dump(soundness_results, f)
            print_and_log("😊  File saved to {} 😊".format(result_path))
    else:
        # The above code is printing a message and logging it. The message states that the file
        # already exists and it will not be overwritten. The smiley face emoji at the end of the
        # message indicates a positive or happy tone.
        print_and_log("⚠️  File {} already exists, not overwriting ⚠️".format(result_path))

    # Now, let's try to overwrite with an added pass at k
    # Calculate pass@k.
    to_print = ''
    total = np.array([r["nfiles"] for r in soundness_results["eval"].values()])
    base_correct = []
    new_correct = []
    
    print_and_log("😊  Calculating pass@k 😊".format(result_path))

    for res in soundness_results["eval"].values():
        bc = sum([r[0] == SUCCESS for r in res["base"]])
        base_correct.append(bc)
        if len(res["plus"]) > 0:
            new_correct.append(
                sum(
                    [
                        res["plus"][i][0] == res["base"][i][0] == SUCCESS
                        for i in range(len(res["plus"]))
                    ]
                )
            )
    base_correct = np.array(base_correct)

    pass_at_k = {
        f"pass@{k}": estimate_pass_at_k(total, base_correct, k).mean()
        for k in [1, 5, 10, 100, 200]
        if total.min() >= k
    }
    to_print += "Base\n" + str(pass_at_k) + '\n'

    if len(new_correct) > 0:
        pass_at_k = {
            f"pass@{k}": estimate_pass_at_k(total, np.array(new_correct), k).mean()
            for k in [1, 5, 10, 100, 200]
            if (total >= k).all()
        }
        to_print += "Base + Extra\n" + str(pass_at_k) + '\n'
    print_and_log(to_print)
    
    with open(os.path.join(log.OUTPUT_FOLDER, "pass_at_k.txt"), "w") as f:
        f.write(to_print)
    
    return soundness_results

def reformat_soundness_results(soundness_results, dataset):
    to_return = []
    for task_id, results in soundness_results['eval'].items():
        for i in range(len(results['base'])):
            this_post = {}
            this_post['task_id'] = task_id
            this_post['response_num'] = results['llm_response_num'][i]
            
            this_post['test_set_correct'] = (results['base'][i][0] == SUCCESS and (results['plus'][i][0] == SUCCESS if dataset =="humanevalplus" else True))
            this_post['base_error'] = None
            
            if len(results['base'][i][2]) > 0 and results['base'][i][2][-1].find('!!BASE ERROR') >= 0:
                this_post['base_error'] = results['base'][i][2][-1]
            
            elif dataset=="humanevalplus" and len(results['plus'][i][2]) > 0 and results['plus'][i][2][-1].find('!!BASE ERROR') >= 0:
                this_post['base_error'] = results['plus'][i][2][-1]
            
            if this_post['test_set_correct']:
                this_post['num_bopi_run'] = 'TBD'
                this_post['num_bopi_killed'] = 'TBD'
            this_post['post_condition'] = results['postcondition_alone'][i]
            this_post['entry_point'] = results['entry_point'][i]
            this_post["all_time_limits"] = results["ref_time"]
            to_return.append(this_post)
    return to_return

class summaryStats():
    def __init__(self):
        self.num_correct = 0
        self.num_correct_per_problem = {}
        self.num_problems_with_one_correct = 0
        self.max_correct_score_per_problem = {}
        self.num_complete = 0
        self.num_bug_complete = 0
        self.num_complete_per_problem = {}
        self.num_bug_complete_per_problem = {}
        self.num_problems_with_one_complete = 0
        self.num_problems_with_one_bug_complete = 0
        self.num_union_complete_per_problem = {}
        self.num_union_bug_complete_per_problem = {}
        self.num_problems_with_union_complete = 0
        self.num_problems_with_union_bug_complete = 0
        self.max_union_correct_score_per_problem = {}
        self.all_scores = {}
        
        #code-specific variables
        self.all_code_scores = {}
        self.max_correct_code_score_per_problem = {}
        self.max_union_correct_code_score_per_problem = {}
        
        #natural code-specific variables
        self.all_natural_code_scores = {}
        self.max_correct_natural_code_score_per_problem = {}
        
        # - see if it's getting the base tests for completeness 
        self.tests_not_yet_killed = {}
        self.codes_not_yet_killed = {}
        
        # Base error stuff
        self.total_num_base_errors = 0
        self.total_num_base_errors_per_problem = {}
        self.num_with_only_base_errors = 0
    
    def update_results(self, post_condition_kill_score, task_id, correct: bool):
        
        if not correct:
            if post_condition_kill_score['base_error'] is not None:
                self.total_num_base_errors += 1
                if task_id not in self.total_num_base_errors_per_problem:
                    self.total_num_base_errors_per_problem[task_id] = 0
                self.total_num_base_errors_per_problem[task_id] += 1
                if self.total_num_base_errors_per_problem[task_id] == 10:
                    self.num_with_only_base_errors += 1
            return
        
        self.num_correct += 1
        if task_id not in self.num_correct_per_problem:
            self.num_correct_per_problem[task_id] = 0
            self.num_problems_with_one_correct += 1
        self.num_correct_per_problem[task_id] += 1
        
        assert(post_condition_kill_score[task_id]['num_tests_run'] >= post_condition_kill_score[task_id]['num_tests_killed'])
        this_score = post_condition_kill_score[task_id]['num_tests_killed'] / post_condition_kill_score[task_id]['num_tests_run']
        
        assert(post_condition_kill_score[task_id]['num_codes_run'] >= post_condition_kill_score[task_id]['num_codes_killed'])
        this_code_score = post_condition_kill_score[task_id]['num_codes_killed'] / post_condition_kill_score[task_id]['num_codes_run']
        
        
        assert(post_condition_kill_score[task_id]['num_natural_codes_run'] >= post_condition_kill_score[task_id]['num_natural_codes_killed'])
        if post_condition_kill_score[task_id]['num_natural_codes_run'] == 0:
            this_nat_code_score = None
        else:
            this_nat_code_score = post_condition_kill_score[task_id]['num_natural_codes_killed'] / post_condition_kill_score[task_id]['num_natural_codes_run']
        
        if task_id not in self.max_correct_natural_code_score_per_problem:
            if this_nat_code_score is not None:
                self.max_correct_natural_code_score_per_problem[task_id] = this_nat_code_score
                self.all_natural_code_scores[task_id] = [this_nat_code_score]
        elif this_nat_code_score is not None:
            self.max_correct_natural_code_score_per_problem[task_id] = max(self.max_correct_natural_code_score_per_problem[task_id], this_nat_code_score)
            self.all_natural_code_scores[task_id].append(this_nat_code_score)
        
        if task_id not in self.max_correct_score_per_problem:
            self.max_correct_score_per_problem[task_id] = this_score
            self.max_correct_code_score_per_problem[task_id] = this_code_score
            self.all_scores[task_id] = [this_score]
            self.all_code_scores[task_id] = [this_code_score]
        else:
            self.all_scores[task_id].append(this_score)
            self.all_code_scores[task_id].append(this_code_score)
            self.max_correct_score_per_problem[task_id] = max(self.max_correct_score_per_problem[task_id], this_score)
            self.max_correct_code_score_per_problem[task_id] = max(self.max_correct_code_score_per_problem[task_id], this_code_score)
        
        if post_condition_kill_score[task_id]['num_tests_run'] == post_condition_kill_score[task_id]['num_tests_killed']:
            self.num_complete += 1
            if task_id not in self.num_complete_per_problem:
                self.num_complete_per_problem[task_id] = 0
                self.num_problems_with_one_complete += 1
            self.num_complete_per_problem[task_id] += 1
        
        if post_condition_kill_score[task_id]['num_codes_run'] == post_condition_kill_score[task_id]['num_codes_killed']:
            self.num_bug_complete += 1
            if task_id not in self.num_bug_complete_per_problem:
                self.num_bug_complete_per_problem[task_id] = 0
                self.num_problems_with_one_bug_complete += 1
            self.num_bug_complete_per_problem[task_id] += 1
        
        if task_id not in self.tests_not_yet_killed:
            self.tests_not_yet_killed[task_id] = []
            self.codes_not_yet_killed[task_id] = set()
            for indx, program in enumerate(post_condition_kill_score[task_id]['test_results']):
                not_yet_killed = set()
                if program[0] != "killed at least one mutant":
                    self.codes_not_yet_killed[task_id].add(indx)
                for i, val in enumerate(program[1]):
                    if val == 0:
                        not_yet_killed.add(i)
                self.tests_not_yet_killed[task_id].append(not_yet_killed)
        else:
            for i, program in enumerate(post_condition_kill_score[task_id]['test_results']):
                not_yet_killed = set()
                if i in self.codes_not_yet_killed[task_id] and program[0] == "killed at least one mutant":
                    self.codes_not_yet_killed[task_id].remove(i)
                for j, val in enumerate(program[1]):
                    if val == 0:
                        not_yet_killed.add(j)
                self.tests_not_yet_killed[task_id][i] = self.tests_not_yet_killed[task_id][i].intersection(not_yet_killed)
                
        
        # If all of those tests are killed, then we can add one to the union complete
        num_not_yet_killed = sum([len(x) for x in self.tests_not_yet_killed[task_id]])
        if num_not_yet_killed == 0:
            if task_id not in self.num_union_complete_per_problem:
                self.num_union_complete_per_problem[task_id] = 0
                self.num_problems_with_union_complete += 1
            self.num_union_complete_per_problem[task_id] = True
        
        num_codes_not_yet_killed = len(self.codes_not_yet_killed[task_id])
        if num_codes_not_yet_killed == 0:
            if task_id not in self.num_union_bug_complete_per_problem:
                self.num_union_bug_complete_per_problem[task_id] = 0
                self.num_problems_with_union_bug_complete += 1
            self.num_union_bug_complete_per_problem[task_id] = True
        
        # Update the max union correct score
        this_union_score = (post_condition_kill_score[task_id]['num_tests_run'] - num_not_yet_killed) / post_condition_kill_score[task_id]['num_tests_run']
        this_union_code_score = (post_condition_kill_score[task_id]['num_codes_run'] - len(self.codes_not_yet_killed[task_id])) / post_condition_kill_score[task_id]['num_codes_run']
        if task_id not in self.max_union_correct_score_per_problem:
            self.max_union_correct_score_per_problem[task_id] = this_union_score
            self.max_union_correct_code_score_per_problem[task_id] = this_union_code_score
        else:
            self.max_union_correct_score_per_problem[task_id] = max(self.max_union_correct_score_per_problem[task_id], this_union_score)
            self.max_union_correct_code_score_per_problem[task_id] = max(self.max_union_correct_code_score_per_problem[task_id], this_union_code_score)
        
    def return_printable_summary(self):
        # This function returns a human readable print of all of the stats that we computed
        to_return = ""
        to_return += "Number of correct post conditions (out of 1640): {}\n".format(self.num_correct)
        to_return += "Number of complete post conditions (out of 1640): {}\n".format(self.num_complete)
        to_return += "Number of bug complete post conditions (out of 1640): {}\n".format(self.num_bug_complete)
        to_return += "Number of post conditions with a base error (out of 1640): {}\n".format(self.total_num_base_errors)
        to_return += "\n"
        to_return += "Number of problems with one correct post condition (out of 164): {}\n".format(self.num_problems_with_one_correct)
        to_return += "Number of problems with one complete post condition (out of 164): {}\n".format(self.num_problems_with_one_complete)
        to_return += "Number of problems with union complete post conditions (out of 164): {}\n".format(self.num_problems_with_union_complete)
        to_return += "Number of problems with one bug complete post condition (out of 164): {}\n".format(self.num_problems_with_one_bug_complete)
        to_return += "Number of problems with one union bug complete post condition (out of 164): {}\n".format(self.num_problems_with_union_bug_complete)
        to_return += "Number of problems with only base errors: {}\n".format(self.num_with_only_base_errors)
        to_return += "\n"
        to_return += "First looking at test-based scores:\n"
        to_return += "Average score for one post condition: {}\n".format(sum([sum(x) for x in self.all_scores.values()]) / sum([len(x) for x in self.all_scores.values()]))
        
        # For this one, first calculate the average score per problem, then average those
        to_return += "Average score for one post condition per problem: {}\n".format(sum([sum(x) / len(x) for x in self.all_scores.values()]) / len(self.all_scores))
        to_return += "Average max correct score for one post condition per problem: {}\n".format(sum(self.max_correct_score_per_problem.values()) / len(self.max_correct_score_per_problem))
        to_return += "Average max union correct score per problem: {}\n".format(sum(self.max_union_correct_score_per_problem.values()) / len(self.max_union_correct_score_per_problem))
        to_return += "\n"
        to_return += "Now, looking at the code-based score:\n"
        to_return += "Average score for one post condition: {}\n".format(sum([sum(x) for x in self.all_code_scores.values()]) / sum([len(x) for x in self.all_code_scores.values()]))
        
        # For this one, first calculate the average score per problem, then average those
        to_return += "Average score for one post condition per problem: {}\n".format(sum([sum(x) / len(x) for x in self.all_code_scores.values()]) / len(self.all_code_scores))
        to_return += "Average max correct score for one post condition per problem: {}\n".format(sum(self.max_correct_code_score_per_problem.values()) / len(self.max_correct_code_score_per_problem))
        to_return += "Average max union correct score per problem: {}\n".format(sum(self.max_union_correct_code_score_per_problem.values()) / len(self.max_union_correct_code_score_per_problem))
        to_return += "\n"
        to_return += "Finally, a couple of natural code scores:\n"
        to_return += "Average score for one post condition: {}\n".format(sum([sum(x) for x in self.all_natural_code_scores.values()]) / sum([len(x) for x in self.all_natural_code_scores.values()]))
        
        # For this one, first calculate the average score per problem, then average those
        to_return += "Average score for one post condition per problem: {}\n".format(sum([sum(x) / len(x) for x in self.all_natural_code_scores.values()]) / len(self.all_natural_code_scores))
        to_return += "Average max correct score for one post condition per problem: {}\n".format(sum(self.max_correct_natural_code_score_per_problem.values()) / len(self.max_correct_natural_code_score_per_problem))
        to_return += "\n"
        to_return += "Number of correct post conditions per problem:\n"
        to_return += "\n".join(["\t{}: {}".format(x, self.num_correct_per_problem[x]) for x in self.num_correct_per_problem])
        to_return += "\n"
        to_return += "Number of complete post conditions per problem:\n"
        to_return += "\n".join(["\t{}: {}".format(x, self.num_complete_per_problem[x]) for x in self.num_complete_per_problem])
        to_return += "\n"
        to_return += "Number of problems with union complete post conditions:\n"
        to_return += "\n".join(["\t{}: {}".format(x, self.num_union_complete_per_problem[x]) for x in self.num_union_complete_per_problem])
        to_return += "\n"
        to_return += "Max correct score for one post condition per problem:\n"
        to_return += "\n".join(["\t{}: {}".format(x, self.max_correct_score_per_problem[x]) for x in self.max_correct_score_per_problem])
        to_return += "\n"
        to_return += "Max union correct score per problem:\n"
        to_return += "\n".join(["\t{}: {}".format(x, self.max_union_correct_score_per_problem[x]) for x in self.max_union_correct_score_per_problem])   
        to_return += "\n"
        to_return += "Number of base errors per problem:\n"
        to_return += "\n".join(["\t{}: {}".format(x, self.total_num_base_errors_per_problem[x]) for x in self.total_num_base_errors_per_problem])
        return to_return        
    

def runEvalofPostconditions(flags, postcondition_sample_dir, output_dir, problems):
    
    # First, set up the number of parallel workers
    if flags.parallel is None:
        n_workers = max(1, multiprocessing.cpu_count() // 2)
    else:
        n_workers = flags.parallel
        
    print_and_log, log_only = log.setup_output_dir(output_dir, subfolder="individual_postcondition_results")
    print_and_log("⚒️  Working directory : {}".format(log.OUTPUT_FOLDER))
    print_and_log(log.make_header("🐈‍⬛  Setting up the output directory  🐈‍⬛"))
        
    # See if the results are sound for this post condition
    print_and_log(log.make_header("🐈‍⬛  Running Soundness Evaluation using {} 🐈‍⬛").format(flags.dataset))

    soundness_results = evaluate_post_condition_soundness(flags, n_workers, postcondition_sample_dir, print_and_log, log_only, problems)
    
    # Now, turn these soundness results into the format we want for the "how powerful is this post condition" results
    print_and_log(log.make_header("🐈‍⬛  Reformatting soundness results for next eval 🐈‍⬛"))
        
    # The whole goal of this is to create a chart that says how many mutants each post condition kills -> here is the base of that chart
    to_return = reformat_soundness_results(soundness_results, flags.dataset)
    
    # Now, let's load the buggy codes
    print_and_log(log.make_header("🐈‍⬛  Running Power Evaluation 🐈‍⬛"))

    print_and_log("😊  Loading buggy codes 😊")
    with open(flags.samples_buggy_codes, 'r') as f:
        buggy_codes = [json.loads(line) for line in f]

    print_and_log("😊  Evaluating each correct post condition 😊")
    stats = summaryStats()
    for i, postcondition_info in enumerate(to_return):
    
        # If the post condition is not sound, then there is no point seeing how powerful it is
        task_id = postcondition_info['task_id']
        correct = postcondition_info['test_set_correct']
        if not correct:
            del to_return[i]['all_time_limits'] 
            stats.update_results(postcondition_info, task_id, False)
            continue

        print_and_log("😊  Evaluating {}, postcondition {} 😊".format(task_id, postcondition_info["response_num"]))
        num_base_tests = len(problems[task_id]['base_input'])
        raw_postcondition = postcondition_info['post_condition']
        sanitized_postcondition = code_sanitize(raw_postcondition)

        if not sanitized_postcondition: 
            continue
        
        entry_point = postcondition_info['entry_point']
        wrapped_codes = []
        for buggy_code in buggy_codes:
            if task_id == buggy_code['task_id']:
                # Wrap the post condition around this buggy code
                wrapped_code = wrap_code_solution(None, buggy_code['solution'], entry_point, sanitized_postcondition)
                # Sanitize the post condition
                buggy_code["wrapped"] = wrapped_code
                wrapped_codes.append(buggy_code)
                 
        # In this case, there are no codes with eligible bad output producing inputs
        # May use this to skip certain problems or post conditions? but for now, just continue
        if len(wrapped_codes) == 0: 
            print("None of the buggy codes had eligible bad output producing inputs for this problem - skipping evaluation: ")
            print(task_id)
            print("Press any key to continue")
            input()
            continue
        #input()
        post_condition_kill_score = evaluate_post_condition_power(wrapped_codes, postcondition_info, n_workers, flags, print_and_log)
        #input()
        to_return[i]['num_bopi_run'] = post_condition_kill_score[task_id]['num_tests_run']
        to_return[i]['num_bopi_killed'] = post_condition_kill_score[task_id]['num_tests_killed']
        
        to_return[i]['num_codes_run'] = len(post_condition_kill_score[task_id]["test_results"])
        to_return[i]['num_codes_killed'] = len([x for x in post_condition_kill_score[task_id]["test_results"] if x[0] == "killed at least one mutant"])
        post_condition_kill_score[task_id]["num_codes_run"] = to_return[i]['num_codes_run'] 
        post_condition_kill_score[task_id]["num_codes_killed"] = to_return[i]['num_codes_killed'] 
        
        to_return[i]['num_natural_codes_run'] = min(len(post_condition_kill_score[task_id]["test_results"]), \
                                                    len([x for x in post_condition_kill_score[task_id]["buggy_code_response_num"] if x < 200]))
        to_return[i]['num_natural_codes_killed'] = len([x for x in post_condition_kill_score[task_id]["test_results"][:to_return[i]['num_natural_codes_run']] if x[0] == "killed at least one mutant"])
        post_condition_kill_score[task_id]["num_natural_codes_run"] = to_return[i]['num_natural_codes_run'] 
        post_condition_kill_score[task_id]["num_natural_codes_killed"] = to_return[i]['num_natural_codes_killed'] 
        stats.update_results(post_condition_kill_score, task_id, True)
        del to_return[i]['all_time_limits']
    
    print_and_log(log.make_header("🐈‍⬛  Finished Running Power Evaluation 🐈‍⬛"))

    power_stats_file = os.path.join(log.OUTPUT_FOLDER, "power_eval_stats.txt")
    print_and_log("😊  Saving power stats to {} 😊".format(power_stats_file))

    stats_results = stats.return_printable_summary()
    with open(power_stats_file, 'w') as f:
        f.write(stats_results)

    all_output_file = os.path.join(log.OUTPUT_FOLDER, "summary_eval_results.jsonl")
    print_and_log("😊  Saving results to {} 😊".format(all_output_file))

    with open(all_output_file, 'w') as f:
        for line in to_return:
            f.write(json.dumps(line) + '\n')
        
    print_and_log(log.make_header("🐈‍⬛ Summary saved successfully! 🐈‍⬛"))
    print_and_log("🐈‍⬛  Done! 🐈‍⬛")   
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, type=str)
    parser.add_argument("--samples-buggy-codes", required=True, type=str)
    parser.add_argument("--samples-post-conditions", required=True, type=str) 
    parser.add_argument("--base-only", action="store_true")
    parser.add_argument("--parallel", default=None, type=int)
    parser.add_argument("--i-just-wanna-run", action="store_true")
    parser.add_argument("--test-details", action="store_true")
    parser.add_argument("--min-time-limit", default=0.2, type=float)
    parser.add_argument("--gt-time-limit-factor", default=2.0, type=float)
    parser.add_argument("--mini", action="store_true")
    parser.add_argument("--insert_alt_ground_truth", action="store_true")
    args = parser.parse_args()

    if not (args.dataset.lower() == "evalplus"):
        raise NotImplementedError("Unsupported dataset: {}".format(args.dataset))
    
    print(args.samples_post_conditions)
    assert os.path.isdir(args.samples_post_conditions), "Post condition folder does not exist or is a file not a folder"
    assert os.path.isfile(args.samples_buggy_codes), "Buggy codes file does not exist or is a folder not a file"
        
    # Now figure out where to save the results
    #output_folder = "/app/postConditionEvalResults"
    output_folder = args.samples_post_conditions.replace("evalDir", "app")
    #output_folder = output_folder.replace("postConditionRuns", "postConditionEvalResults_" + args.dataset) 
    output_folder += "_evalResults_" + args.dataset
    
    if os.path.isdir(output_folder):
        print("Output folder is {}".format(output_folder))
        print("Warning, output folder already exists. Do you want to delete it? (y/n)")
        inp = input()
        if inp == 'y':
            shutil.rmtree(output_folder)
        else:
            print("Do you want to write to a different folder instead? (y/n)")
            inp = input()
            if inp == 'y':
                print("Please enter the new folder name:")
                inp = input()
                output_folder = '/app/' + inp
                
    os.makedirs(output_folder, exist_ok=True)
    

    multirunFile = os.path.join(args.samples_post_conditions, 'multirun.yaml')
    if os.path.exists(multirunFile):
        main_log = log.make_print_and_log_function(os.path.join(output_folder, "main_log.txt"))
        main_log("🪅  Multirun.yaml exists in the directory:\n{}\nProcessing all folders...".format(args.samples_post_conditions))
        
        main_log("⚒️  Now, loading in humaneval...")
        problems = get_human_eval_plus(mini=args.mini)
        main_log("🪅😍😍  Success!! 😍😍🪅")

        for multirunFolder in os.listdir(args.samples_post_conditions):
            if multirunFolder == 'multirun.yaml': continue
            if multirunFolder == 'response_preprocessing.log': continue
            if multirunFolder == 'main_log.txt': continue
            if multirunFolder == '.DS_Store': continue
            if multirunFolder == '.hydra':
                # Copy this folder to the output folder
                main_log("\t🐝 Copying hydra config: {}".format(os.path.join(args.samples_post_conditions, multirunFolder)))
                shutil.copytree(os.path.join(args.samples_post_conditions, multirunFolder), os.path.join(output_folder, multirunFolder + '_copy'), dirs_exist_ok=True)
                continue
            
            assert int(multirunFolder) >=0, "Folder name is not a number, malformed samples folder!!: {}".format(multirunFolder)
            main_log("\tNow processing subfolder: {}".format(multirunFolder))
            postcondition_sample_dir = os.path.join(args.samples_post_conditions, multirunFolder)
            this_output_folder = os.path.join(output_folder, multirunFolder)
            runEvalofPostconditions(args, postcondition_sample_dir, this_output_folder, problems)
    else:
        main_log = log.make_print_and_log_function(os.path.join(output_folder, "main_log.txt"))
        main_log("⚒️  Now, loading in humaneval...")
        problems = get_human_eval_plus(mini=args.mini)
        main_log("🪅😍😍  Success!! 😍😍🪅")
        runEvalofPostconditions(args, args.samples_post_conditions, output_folder, problems)

        
if __name__ == "__main__":
    main()

