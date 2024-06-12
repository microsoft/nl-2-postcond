"""
This file is used to generate sample completions using the LLM model for a given prompt.
"""
from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.types import RunMode
from evalplus.data import write_jsonl
import os
import openai
import time
from decouple import config
from tenacity import retry, stop_after_attempt, wait_fixed, wait_random_exponential,  retry_if_exception_type
import json
import prompts
import log
from log import make_header
import sys
from benchmarks import load_benchmarks


def setup_api(api_cfg, print_and_log):
    """
    Sets up the api with the api type and API key
    You should modify this for the specific model you are using
    """
    
    if api_cfg.name == "azure":
        openai.api_type = api_cfg.name
        openai.api_base = api_cfg.base
        openai.api_version = api_cfg.version
        openai.api_key = config(api_cfg.key)
        assert openai.api_key != None, "API key not found. Please set the {} environment variable.".format(api_cfg.key)
    
    elif api_cfg.name == "openai":
        openai.api_key = config(api_cfg.key)
        assert openai.api_key != None, "API key not found. Please set the {} environment variable.".format(api_cfg.key)
    
    else:
        raise ValueError("Invalid API name: {}".format(api_cfg.name))
    

def load_postconditions(evaluated_post_conditions_file):
    with open(evaluated_post_conditions_file, 'r') as f:
        evals = [json.loads(line) for line in f]
    
    postconditions = {}
    for e in evals:
        if e['task_id'] not in postconditions:
            postconditions[e['task_id']] = [e]
        else:
            postconditions[e['task_id']].append(e)
            
    # assert that each task_id has the same number of postconditions
    assert len(set([len(postconditions[k]) for k in postconditions])) == 1, "Uneven number of postconditions per task_id"
    return postconditions 


def prepare_prompt(exper_cfg, problem) -> str:

    # Set all of the default values
    toGenerateFull = ''
    toGenerateShort = ''
    toGenerateGoal = ''
    toUse = ''
    toGenerateShortCaps = ''
    promptAdds = ''
    entrypoint = problem["entry_point"]
    code = problem["prompt"]

    # If we are doing the code generation task (used to generate buggy code mutants)
    if exper_cfg.to_generate == "code":
        if exper_cfg.gen_buggy == False:
            return prompts.genCode.substitute(
                codeStubAndDocstring=code,
                entrypoint=entrypoint)
        else:
            return prompts.genCodeBuggy.substitute(
                codeStubAndDocstring=code,
                entrypoint=entrypoint) 
        
    if exper_cfg.has_reference_code:
        code += problem["canonical_solution"]
        promptTemplate = prompts.genOneWithRef[exper_cfg.prompt_v]
    else: 
        promptTemplate = prompts.genOneNoRef[exper_cfg.prompt_v]

    if exper_cfg.to_generate == "postcondition":
        toGenerateFull = "symbolic postcondition"
        toGenerateShort = "postcondition"
        toGenerateGoal = "means"
        toGenerateShortCaps = "Postcondition".upper() 
    else:
        raise NotImplementedError

    if exper_cfg.prompt_v == "base":
        return promptTemplate.substitute(
                codeStubAndDocstring=code,
                toGenerateFull= toGenerateFull, 
                toGenerateShort=toGenerateShort, 
                toGenerateGoal=toGenerateGoal,  
                toGenerateShortCaps=toGenerateShortCaps,
                promptAdds=promptAdds,
                entrypoint=entrypoint)

    elif exper_cfg.prompt_v == "simple":
        return promptTemplate.substitute(
            codeStubAndDocstring=code,
            toGenerateFull= toGenerateFull, 
            toGenerateShort=toGenerateShort, 
            toGenerateShortCaps=toGenerateShortCaps,
            entrypoint=entrypoint)
    

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(2000))
def ask(prompt, exper_cfg, log_only):
    """
    This function returns the response from the API call - can be modified to support additional models 
    """

    log_only("Attempting call...")
    # FIXME - this is what you will need to change for the open source model
    if exper_cfg.model.startswith("gpt-3"):
        response = openai.ChatCompletion.create(
        engine=exper_cfg.model, 
        messages=[
            {"role": "system", "content": exper_cfg.system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=exper_cfg.temperature,
        n=exper_cfg.n_model_responses,
    )
    else:
        response = openai.ChatCompletion.create(
        model=exper_cfg.model, 
        messages=[
            {"role": "system", "content": exper_cfg.system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=exper_cfg.temperature,
        n=exper_cfg.n_model_responses,
    )

    return response

def generate_one_completion(exper_cfg, problem, task_id, run_num, log_only, postconditions=None):
    """
    This function gets and processes one call from the API
    """

    prompt = prepare_prompt(exper_cfg, problem)
        
    log_only("🪅  Generating {} responses for the following prompt: \n {}".format(exper_cfg.n_model_responses, prompt))

    try:
        #time.sleep(10)
        response = ask(prompt, exper_cfg, log_only)
        #break # if we get a response, break out of the loop
    except Exception as e:

        log_only("################### ERROR for {}, {} ###################".format(task_id, exper_cfg.to_generate))
        log_only("Error for {}: {}".format(task_id, str(e)))
        log_only('\n\n\n')
        log_only('Even with retries, not able to generate for ' + task_id, str(e))
        return None
    
    # Log the response
    log_only("################### FULL RESPONSE for {}, {} ###################".format(task_id, exper_cfg.to_generate))
    log_only(json.dumps(response, sort_keys=True))
    log_only("################### ONE ANSWER for {}, {} ###################".format(task_id, exper_cfg.to_generate))
    log_only(response["choices"][0]["message"]["content"])
    log_only('\n\n\n')

    all_out = ''

    # Make human readable files as a byproduct
    # First, a human readable file for each response
    program_dir = os.path.join(log.OUTPUT_FOLDER, log.SUB_FOLDER)
    print(log.OUTPUT_FOLDER, log.SUB_FOLDER)
    for i in range(len(response["choices"])):

        file_base = task_id.replace('/', '_') + '_' + exper_cfg.to_generate + '_' 
        with open(os.path.join(program_dir, file_base + str(i + run_num*exper_cfg.n_per_model_call) + '.py'), 'w') as f:
            thisResponse = response["choices"][i]["message"]["content"]
            f.write(thisResponse + '\n\n\n')
            all_out += '\n# Response ' + str(i) + '\n' + thisResponse +  '\n\n\n'
            f.flush()
            os.fsync(f.fileno())

    # Second, a file with all responses combined
    with open(os.path.join(program_dir, file_base + '_all.py'), 'w') as f:
        f.write(all_out)
        f.flush()
        os.fsync(f.fileno())

    print('Finished problem ' + str(task_id))
    response['version'] = exper_cfg.to_generate
    return response   

@hydra.main(version_base=None, config_path="./config", config_name="config")
def main(cfg):

    #set up the output folder
    hydra_cfg = hydra.core.hydra_config.HydraConfig.get()
    #if hydra_cfg.mode != RunMode.MULTIRUN:
    #    os.chdir(hydra_cfg.runtime.output_dir)
    print_and_log, log_only = log.setup_output_dir(hydra_cfg)

    print_and_log("Working directory : {}".format(os.getcwd()))
    print_and_log(make_header("Setting up output folder..."))

    # print the config file to standard out (this will also be dumped into the outputs folder)
    print_and_log(make_header("Loaded Config"))
    print_and_log(OmegaConf.to_yaml(cfg))

    # set up the model
    print_and_log(make_header("Setting up {} API...".format(cfg.api.name)))
    setup_api(cfg.api, print_and_log)
    print_and_log(make_header("Successfully set up {} API".format(cfg.api.name)))

    # load benchmark problems
    print_and_log(make_header("Loading benchmark problems from {}...".format(cfg.benchmarks.name)))
    problems = load_benchmarks(cfg.benchmarks)
    print_and_log(make_header("Successfully loaded {} problems".format(len(problems))))
    
    # If we are generating rankings, load the postconditions
    if cfg.experiment.to_generate == "rank":
        print_and_log(make_header("Loading postconditions..."))
        all_postconditions = load_postconditions(cfg.experiment.evaluated_post_conditions_file)
        print_and_log(make_header("Successfully loaded {} postconditions".format(len(all_postconditions))))

    # generate model completions for each problem
    print_and_log(make_header("Generating Code for {} prompts... ".format(len(problems))))
    
    samples = []

    this_postconditions = None
    
    doRun = True
    
    if cfg.benchmarks.run_range and cfg.benchmarks.run_start != "HumanEval/0":
        doRun = False

        
    for task_id in problems:
        print(cfg.benchmarks.run_start, task_id)    

        if cfg.benchmarks.run_range and task_id == cfg.benchmarks.run_start:
            doRun = True
            
        if not doRun: 
            continue
        
        for i in range(cfg.experiment.n_per_model_call):
            sample = dict(
                task_id=task_id, 
                run_num=i,
                completion_pre=generate_one_completion(cfg.experiment, problems[task_id], task_id, i, log_only, this_postconditions)
            )

            write_jsonl(os.path.join(log.OUTPUT_FOLDER,"samples_partial.jsonl"), [sample], append=True)
            samples.append(sample)
        
        if cfg.benchmarks.run_range and task_id == cfg.benchmarks.run_end:
            doRun = False


    print_and_log(make_header("COMPLETED CODE GENERATION, SAVING JSONL FILE..."))

    # save the completions to the output folder in json format
    print(cfg.experiment.to_generate)
    print(samples)
    write_jsonl(os.path.join(log.OUTPUT_FOLDER, "samples_{}.jsonl".format(cfg.experiment.to_generate)), samples)

    print_and_log(make_header("JSON SAVED, DONE"))


if __name__ == "__main__":
    if 'hydra.mode=MULTIRUN' in sys.argv:
        sys.argv.append('hydra.sweep.dir=multirun_llm_gen/${now:%Y-%m-%d}/${now:%H-%M-%S}')
    else:
        sys.argv.append('hydra.run.dir=llm_gen_outputs/${now:%Y-%m-%d}/${now:%H-%M-%S}')
    main()
