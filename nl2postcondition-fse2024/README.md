# nl2postcondition

Natural language to program postcondition generation

FSE'24 paper artefacts. 


This repository contains the replication materials for the paper, 

*Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions?*

to appear in Foundations of Software Engineering (FSE), 2024

Authors:    Madeline Endres (University of Michigan)
            Sarah Fakhoury (Microsoft Research);
            Saikat Chakraborty (Microsoft Research);
            Shuvendu Lahiri (Microsoft Research)

A preprint of the paper is available here: https://arxiv.org/pdf/2310.01831

This repository contains the following:

All LLM prompts and postconditions analyzed for the FSE paper
The set of code-mutants produced for the FSE paper
Qualitative analysis spreadsheet
Analysis scripts + docker container for running the nl2postcondition with EvalPlus

Subfolders of this repository contains their own READMEs with more detailed instructions if needed. The layout of this repository is:

* [GeneratedPostconditions](GeneratedPostconditions/README.md): All generated postconditions analyzed in the FSE paper, along with their evaluation results and logs. Includes both EvalPlus and Defects4J results.
* [QualitativeAnalysis](QualitativeAnalysis/README.md): A spreadsheet with the results of our manual analysis of a subset of EvalPlus postconditions
* [PromptTemplates](PromptTemplates/README.md): Contains all prompts ablations used for both EvalPlus and Defects4J. 
* [nl2postcondition_source_evalplus](nl2postcondition_source_evalplus/README.md): All nl2postcondition code for the EvalPlus benchmark. Includes scripts for postcondition generation, postcondition preprocessing, and postcondition evaluation.

Due to integration with other internal projects, the source code for the Defects4J evaluation is not yet public.



