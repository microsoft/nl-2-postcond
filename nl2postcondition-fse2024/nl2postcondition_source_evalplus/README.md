# nl2postcondition - EvalPlus

## Overview

The scripts in this folder allow you to run and evaluate *nl2postcondition* on the [EvalPlus](https://github.com/evalplus/evalplus) benchmark. There are three primary scripts:

1. `llm_sample_generator.py`: This is the file that allows you to generate postconditions for each EvalPlus benchmark problem. It includes our postcondition generation prompts (listed in `prompts.py`).
2. `response_preprocessing.py`: This script transforms the raw llm output into executable postconditions that are inserted into the EvalPlus benchmark problems.
3. `run_postcondition_evaluation.py`: This script evaluates the preprocessed llm-generated postconditions. We highly recommend running this script in the provided docked container (instructions detailed below).

In the rest of this file, we detail the overall setup requirements, and then information regarding how to run each of the three scripts above.

## Setup Instructions:

Before you use the code in this repository, you will need to

1. This project requires Python 3.9 or later. In addition, it requires several Python packages. These can be installed by running:  ```pip install -r requirements.txt```

   *NOTE:* We highly recommend running all code in a virtual environment, eg:
   
   ```
   # Installs virtualenv
   python3 -m pip install virtualenv

   # Makes the env
   python3 -m virtualenv myNl2SpecEnv

   # Then activate the env where you can install all of your requirements
   source myNl2SpecEnv/bin/activate
   ```

3. Create an .env file, and add your API Key. The code is currently implemented for the GPT3.5 azure api, and also the GPT4 OpenAi api.

4. Modify the configuration files as needed for the script you are running. For the configuration manager, we use [Hydra](https://hydra.cc/docs/intro/). Some sample configuration files are included in the `config` folder. However, configuration can also be modified directly at run time. Examples of the configuration options needed for each script are included in this README.

## Experiment types - Human Eval Experiments

We now go through each of the three scripts listed above.

### llm_sample_generator

This the script that can be used to generate postconditions for EvalPlus problems using an LLM. This script is currently the default in the included sample config files (using the azure api). To run it, you can call:

`python llm_sample_generator.py`

However, you may need to change the default configuration, or you want to make your own experiment config file. If so, you can use

`python llm_sample_generator.py experiment=<yourConfigHere>`

Where `<yourConfigHere>` is based on `config/experiment/generateLLMSamples.yaml`

If you would like to change any of the configuration parameters, you can either change them in the config
file itself (see `config/experiment/generateLLMSamples.yaml`), or you can change them at run time at the command line. For example, the default temperature for LLM querries is 0.7. If you want the script to use 0.2 instead, you can run:

`python llm_sample_generator.py experiment.temperature=0.2`

This script contains the following configuration options:

```
config
    api
        azure
            name
            version
            base
            key
        openai
            name
            key
    benchmarks
        evalplus
            run_all: bool
            run_range: bool
            run_start: string
            run_end: string
    experiment
        generateLLMSamples
            model
            temperature
            n_model_responses
            n_per_model_call
            to_generate: string saying postcondition
            has_reference_code: bool
            prompt_v: base or simple
            system_prompt: string
```

Running `llm_sample_generator` will generate a sub-folder organized by time and date inside a folder called `llm_gen_outputs`. In this folder, there is the recording of the config, an experimental log, `samples.jsonl` which contains all of the generated
samples and human-readable files with all of the samples.

### response_preprocessing

Once you have generated the llm responses, you can pre-process them using `response_preprocessing.py`. This will extract the postcondition and wrap it for evaluation

To run:

`python response_preprocessing.py experiment=preprocessSamples.yaml`

Should you want to try running this script without generating postconditions first, we have included the results of one of the experimental runs in the paper in the `llm_gen_outputs` folder. However in practice, you will need to change `samplesFolder` in the `experiment\preprocessSamples.yaml` config file to point to where the samples you generated using the LLM are. This script will make some additional hydra log files, and will store the results in a subfolder called `response_preprocess_outputs`.

### run_postcondition_evaluation

To do this evaluation, you will want to do it in the repository docker container. 

1. First, build the docker container:
   `sudo docker build -t nl2postcondition_eval .`

2. Then make a folder for the results: `mkdir dockerResults`

3. Finally, run the evaluation in the docker container. For a quick run using the example preprocessed outputs included in this repository, you can use the following command: 

```
sudo docker run -it --mount type=bind,source="$(pwd)"/dockerResults,target=/app nl2postcondition_eval --dataset evalplus --samples-buggy-codes /evalDir/distinct_code_mutants.jsonl --samples-post-conditions /evalDir/sample_GPT4Eval --test-details --parallel $(nproc) --gt-t
ime-limit-factor 10.0 --min-time-limit 0.5
```
This command will run both the correctness and completeness evaluations (using a modified version of the evalplus evaluation handler stored in `lib`) for the sample preprocessed postconditions in `response_preprocess_outputs/sample_preprocessedGPT4simpleWithRef`, and will output these results into the folder `dockerResults/sample_GPT4Eval_evalResults_evalplus`. The [README file](../GeneratedPostconditions/README.md#evalplus) file on GeneratedPostconditions explains the output files produced. 

#### Available options for postcondition evaluation script

The following command-line options are available for the postcondition evaluation script:

* `--dataset: string, required`: currently, only `"evalplus"` is supported
* `--samples-buggy-codes: string, required`: This is the loaction of the `jsonl` file that contains the distinct buggy code mutants used in the completeness evaluation. Should you use the provided buggy codes and default docker file, this will always be `"/evalDir/distinct_code_mutants.jsonl"`
* `--samples-post-conditions: string, required`: This is the path to the folder containing the preprocessed postconditions. When using the sample postconditions and default docker container, this is `"/evalDir/sample_GPT4Eval"`. If you would like to evaluate your own postconditions, you will need to modify this argument and the Dockerfile accordingly.
* `parallel: int, optional`: If running in parallel, the number of cores you'd like to use.
* `--min-time-limit: float, optional`: The minimum time to spend evaluating any given postcondition for correctness or completeness
* `--gt-time-limit-factor: float, optional`: the maximum time to spend evaluating any given postcondition for correctness or completeness, represented as a multiple of the expected time for the EvalPlus reference solution. We note that as several of the buggy codes used in our evaluation are less efficient than the reference solution, we recommend using a factor of at least 5. A factor of 10 was used in our evaluation.
* `--i-just-wanna-run: None, optional:` forces the script to ignore cashed files and re-run the evaluation

