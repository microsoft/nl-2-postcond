# base env: py39 ubuntu20.04
FROM python:3.9-slim-buster

# This Dockerfile is used to run the evaluation for nl2postcondition (see the file run_postcondition_evaluation.py)
# To use this to generate new samples, you will need to modify the copy section to have the postconditions you generated in the container
# install git
RUN apt-get update && apt-get install -y git && apt-get install unzip

RUN mkdir /evalDir

# Copy in the code mutants that will be used for the evaluation
COPY code_mutants/distinct_code_mutants.jsonl.zip /evalDir/distinct_code_mutants.jsonl.zip
RUN unzip /evalDir/distinct_code_mutants.jsonl.zip -d /evalDir

# upgrade to latest pip
RUN pip install --upgrade pip

RUN mkdir SpiCoder
WORKDIR /SpiCoder
COPY requirements.txt /SpiCoder/requirements.txt
RUN pip install -r "requirements.txt"

# Make the docker use the modified evalplus evaluation handler
RUN pip uninstall evalplus -y
COPY *.py /SpiCoder/
RUN mkdir lib
COPY lib /SpiCoder/lib
RUN unzip /SpiCoder/lib/evalplusWithNl2PostconditionEval.zip -d /SpiCoder/lib
RUN ls /SpiCoder/lib
RUN ls
RUN pip install /SpiCoder/lib/evalplus

######################################################################################
# MODIFY THIS TO POINT TO THE PREPROCESSED POSTCONDITIONS YOU ARE TRYING TO EVALUATE #
######################################################################################

# Format is:
# COPY preprocessed_samples_loc /evalDir/FOLDER_WHERE_EVAL_RESULTS_WILL_BE

COPY response_preprocess_outputs/sample_preprocessedGPT4simpleWithRef /evalDir/sample_GPT4Eval

######################################################################################
# END MODIFICATIONS                                                                  #
######################################################################################

ENTRYPOINT ["python3", "-m", "run_postcondition_evaluation"]


