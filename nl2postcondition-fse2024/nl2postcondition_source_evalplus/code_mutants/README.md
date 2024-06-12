## Buggy Code Mutants

This folder contains the artificial and natural code mutants, along with the set of unique buggy codes used in our evaluation.

Specifically, we include all generated codes:
* `NaturalMutantCodeGen`: The set of all "natural" codes generated (both correct and buggy) using the standard code-generation prompt (see prompt templates). 200 codes were generated per EvalPlus problem.
* `ArtificialMutantCodeGen`: The set of all "artificially buggy" codes generated using a prompt that asked the LLM to include a bug in the produced program. 100 codes were generated per EvalPlus problem.

As well as some relevant preprocessed files:
* `eval_results_merged_codes.jsonl`: The results of the full EvalPlus run on all llm-generated codes. Contains 300 codes generated per problem. The first 200 are the natural codes, and the last 100 are artificial buggy codes. This EvalPlus run tells us which codes are buggy, and which specific EvalPlus inputs cause the buggy output.
* `merged_codes_preprocessed.jsonl`: These are the preprocessed codes that were used to generate `eval_results_merged_codes.jsonl`.

And then some files that just contain buggy codes:
* `all_code_mutants_with_bad_output.jsonl`: These are the subset of the merged codes that have at least one EvalPlus input that produces bad output (e.g., not the output of the reference solution, and also not an error.) These are the types of failures that a postcondition could potentially catch and discriminate.
* `distinct_code_mutants.jsonl`: These are the subset of buggy codes that contribute at least one unique buggy input/bad output pair. These are the codes used in our evaluation.

