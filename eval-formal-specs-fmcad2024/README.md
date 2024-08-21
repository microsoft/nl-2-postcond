# User intent formalization for verifier-aware languages 
Scripts and benchmarks for the paper 

__Evaluating LLM-driven User-Intent Formalization for Verification-Aware Languages__, *Shuvendu K. Lahiri*.
https://arxiv.org/abs/2406.09757
(Accepted to appear in __FMCAD'2024__ proceedings)

## Installing Dafny
Install binaries from https://github.com/dafny-lang/dafny/wiki/INSTALL
Install Version 4.6 or later
        
## Examples
Install the following repository for the examples:
https://github.com/Mondego/dafny-synthesis.git
Clone the repo at commit a57ce249913c883085401e9072233852826f4e24 (HEAD -> master, origin/master, origin/HEAD)

## Running specification testing harness

`python3 eval_dafny_spec.py --dafny /home/shuvendu/dafny/Scripts/dafny --mutate 5 --file ~/dafny-synthesis/MBPP-DFY-50/test/task_id_594 --log dmp`

To run with a json file with user labels:

`python3 eval_dafny_spec.py --dafny /home/shuvendu/dafny/Scripts/dafny --log dmp --mutate 5 --file ~/dafny-synthesis/MBPP-DFY-50/test/task_id_594 --user-labels-json ~/dafny-synthesis/RQs/RQ3-\[Dynamic-Few-Shot-Prompting\]/rq3-dynamic-few-shot-prompting-GPT-4-temp_0.5-verified-unverified-tagged.json`

Inspect the output for the soundness and completeness for *each* test (and different mutations) and the *overall* score. 

`grep -e Statistics -e label dmp`
        
        //Each line is a test, and the vector denotes number of assertion failures for 
        //[test, test-mutation-1, ...., test-mutation-5] 
        //0: no verification failures, 1: 1 failure 
        
        examples/task_id_2 Dafny Statistics for test: [0, 1, 0, 1, 0, 1] 
        examples/task_id_2 Dafny Statistics for test: [0, 1, 0, 0, 1, 1] 
        examples/task_id_2 Dafny Statistics for test: [0, 0, 1, 0, 1, 1] 
        
        //Overall score across the 3 tests, along with the User label (extracted from the json file) 
        examples/task_id_2 Average Correctness: 1.0, Average Completeness: 0.6, User label: Right postconditions. All good[STRONG-POST][STRONG-INV][CONFIRMED-WITH-TESTS]


## Running an entire folder

`python3 run_mbpp_dafny_dataset.py --folder ~/dafny-synthesis/MBPP-DFY-153/test/`

To run with a json file with user labels:

`python3 run_mbpp_dafny_dataset.py --folder ~/dafny-synthesis/MBPP-DFY-153/test --user-labels-json /home/shuvendu/dafny-synthesis/RQs/RQ3-\[Dynamic-Few-Shot-Prompting\]/rq3-dynamic-few-shot-prompting-GPT-4-temp_0.5-verified-unverified-tagged.json`
