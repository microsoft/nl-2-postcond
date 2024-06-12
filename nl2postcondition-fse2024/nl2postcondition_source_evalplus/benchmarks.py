from evalplus.data import get_human_eval_plus
import json
import os

def load_evalplus_subset(evalplus_cfg):
    """
    Loads a subset of the humaneval+ benchmarks in the right format
    """
    problems = get_human_eval_plus()

    # if we are running all problems, return all problems
    if evalplus_cfg.run_all:
        return problems
    
    # otherwise, we are running a subset of the problems
    # see if we are running a specific subset or excluding a specific subset
    assert len(evalplus_cfg.run_only) > 0 or len(evalplus_cfg.run_except) > 0, "If not running all problems, you must specify either a subset to run or a subset to exclude"
    assert len(evalplus_cfg.run_only) == 0 or len(evalplus_cfg.run_except) == 0, "If not running all problems, you must specify either a subset to run or a subset to exclude, not both"
    
    filtered_problems = {}

    # if we are running a subset of the problems, filter those out
    for key, value in problems.items():
        stim_num = int(key[key.find('/')+1:])
        if len(evalplus_cfg.run_only) > 0 and stim_num in evalplus_cfg.run_only:
            filtered_problems[key] = value
    
        if len(evalplus_cfg.run_except) > 0 and stim_num not in evalplus_cfg.run_except:
            filtered_problems[key] = value

    return filtered_problems



def load_defect4j_bugs(data, ids_set):
    to_return = []
    
    # Loop through all of the files that have been changed
    task_id_base = data["project"] + "_" + data["bugid"]
    
    for path, results in data["method_changes_per_file"].items():
        for result in results:
            this_bug = {}
            this_bug["task_id"] = task_id_base + "_" + path + "_" + "".join(result["buggy"]["signature"].split())
            
            # We can skip these because these are cases when the fix involves adding a function, so only need the one "buggy one"
            if this_bug["task_id"] in ids_set: continue 
            else: ids_set.add(this_bug["task_id"])
            
            this_bug["class_context"] = result["buggy"]["preceding_class_context"]
            this_bug["class_details"] = result["buggy"]["class_details"]
            this_bug["relevant_class_details"] = result["buggy"]["relevant_class_details"]
            this_bug["imports"] = "\n".join(result["buggy"]["relevant_imports"])
            this_bug["method"] = result["buggy"]["code_wo_comment"]
            this_bug["comment"] = result["buggy"]["comment_before_code"].strip()
            this_bug["method_stub"] = result["buggy"]["signature"]
            this_bug["method_name"] = result["buggy"]["signature_short"]
            this_bug["task_order"] = len(ids_set)
            to_return.append(this_bug)
    return to_return
    

def load_defects4j(benchmarks_cfg):
    """_summary_

    Args:
        benchmarks_cfg (_type_): _description_
    """
    bug_metadataFolder = benchmarks_cfg.location

    to_return= []
    the_task_ids = set()
    # Loop through the files in this path, and if they are json files, load each one
    for root, dirs, files in os.walk(bug_metadataFolder):
        for filename in sorted(files):
            if filename.endswith('.json'):
                # Load the json file
                with open(os.path.join(root, filename), 'r') as f:
                    data = json.load(f)
                    to_return.extend(load_defect4j_bugs(data, the_task_ids))
    
    
    # to_return task ids
    to_return_task_ids = [bug["task_id"] for bug in to_return]
    to_return_task_ids_set = set(to_return_task_ids)
        
    return to_return

def load_benchmarks(benchmarks_cfg):
    """
    Loads the benchmark problems from the specified benchmark
    """

    # We are running with evalplus
    if benchmarks_cfg.name == "evalplus":
        
        # load all (or a subset) of the humaneval+ benchmark
        return load_evalplus_subset(benchmarks_cfg)
    elif benchmarks_cfg.name == "Defects4J" or benchmarks_cfg.name=="defects4j":
        return load_defects4j(benchmarks_cfg)
    else:
        raise ValueError("Invalid benchmark name: {}".format(benchmarks_cfg.name))
    
