import sys
import hydra
from hydra.types import RunMode
import log
import os
from evalplus.data import get_human_eval_plus, write_jsonl
import json
from string import Template
import ast
from benchmarks import load_benchmarks
import traceback
import glob
import shutil


"""
This script takes samples generated by llm_sample_generator and combines them with
the human eval benchmark programs to create a new jsonl file in a format that can be used with the modified EvalPlus evaluator

If you are using this script, you should have already generated samples using llm_sample_generator.

If you are using your own generation tool for pre/post conditions, one form human eval can process is:

sample = { 
    'task_id': task_id,
    'solution': sanitized,
    'compiles': true/false,
    'uniqueID': num,
    'isSyntacticDupe': 
}

As json rows in a jsonl file. For any given task id, they should be in the order that they were generated
by your generation tool to get an accurate pass@k.

"""


POSTCONDITION_TEMPLATE = Template("""

def ${entry_point}${argsDec}

    return_value = ${entry_point}_original${argsCall}
    
    # Adding imports that might be useful for postconditions
    import re 
${postcondition}

    return return_value
""")


def load_jsonl(file):
    """
    This loads in the jsonl of raw llm runs such that we have a jsonl file 
    with the same number of lines as the number of samples
    """
    toReturn=[]
    with open(file, 'r') as f:
            
        return [json.loads(line) for line in f]
    
def get_func_args(func: str) -> list:
    """
    Returns the arguments of a function
    """
    func_ast = ast.parse(func)
    func_args = func_ast.body[0].args.args
    return [arg.arg for arg in func_args]

def change_func_name_in_code(code: str, old_name: str, new_name: str) -> str:
    """
    Changes the name of a function in a string of code using ast
    """
    code_ast = ast.parse(code)
    for node in ast.walk(code_ast):
        if isinstance(node, ast.FunctionDef) and node.name == old_name:
            node.name = new_name
    return ast.unparse(code_ast)

def add_missing_imports(code: str) -> str:
    """
    Adds standard python missing imports to a string of code
    """
    pass

def extract_code(rawLLMGen, isOpenSource=False, lang='python'):
    """
    This function extracts generated code from the llm response
    (e.g., removing tik marks, python word, and nat lang text)
    """
    
    # First, count the number of wrapper ticks
    numTicks = rawLLMGen.count('```')

    # No wrapper
    if numTicks == 0 and lang == 'python' and not isOpenSource:
        return rawLLMGen
    
    if numTicks == 0 and lang == 'json' and not isOpenSource:
        return rawLLMGen[rawLLMGen.find('['):rawLLMGen.rfind(']')+1]
    
    # if there is two or more, remove all code after the last one
    if numTicks >= 2:
        parts = rawLLMGen.split('```', 2)  # Split the string at most twice
        assert(len(parts) > 2)
        rawLLMGen = '```'.join(parts[:2])  # Join the first two parts back together with sub

    if lang == 'json':
        return rawLLMGen[rawLLMGen.find('['):rawLLMGen.rfind(']')+1]
    
    # Now, get rid of everything before the first one if it is ```python
    wrapper1='```'+lang
    
    wrapper1_idx = rawLLMGen.find(wrapper1)
    
    # If we find the full wrapper 1 exists
    if wrapper1_idx >= 0:
        rawLLMGen = rawLLMGen[wrapper1_idx + len(wrapper1):]
        
    # at this point, just replace all remaining ``` and move on
    rawLLMGen = rawLLMGen.replace('```', '\n')

    # If we are using the open source model, additional pre-processing is needed due to less standard formatting of responses
    if isOpenSource:

        # First, split by new line and remove all lines that don't start in an assert
        all_lines = rawLLMGen.split('\n')
        
        import_lines = []
        code_lines = []

        for line in all_lines:
            if line.startswith("import") or line.startswith("from"):
                import_lines.append(line)
            if len(code_lines) == 0 and line.startswith("assert"):
                code_lines.append(line)
            elif len(code_lines) > 0 and (line.strip() == "" or line.startswith('#') or line.startswith("'''") or line.startswith("assert")):
                break
            elif len(code_lines) > 0:
                code_lines.append(line)
            
        if len(code_lines) == 0:
            rawLLMGen = "# NO VALID ASSERT PRODUCED, SO RETURNING FALSE\nassert FALSE"
        
        else:
            rawLLMGen = '\n'.join(import_lines) + '\n' + '\n'.join(code_lines)

    return rawLLMGen  
    

def wrap_code_solution(cfg, code_solution: str, entry_point, toAdd: str) -> str:
    """
    This code wraps the code solution in another function s.t. the post condition can
    be tested by human eval
    """
    
    # If we are doing code, just return the code
    if cfg is not None and cfg.sampleType == 'code':
        return toAdd
    
    new_solution = ""
    if cfg is None or cfg.sampleType == 'postcondition' or cfg.sampleType == 'multirun':
        
        # For the post conditions, we will be wrapping the sample function
        # in a function that checks the post condition and returns the result
        new_func_name = entry_point + '_original'

        code_solution = change_func_name_in_code(code_solution, entry_point, new_func_name)
        
        # We are calling this from another file -> prob post condition checker, so do one more change
        if cfg is None:
            code_solution = code_solution.replace(entry_point +'(', new_func_name + '(')
        toAdd = toAdd.replace(entry_point +'(', new_func_name + '(')

        # Get the arguments of the function locations
        func_start_idx = code_solution.find('def ' + new_func_name)
        args_start_idx = func_start_idx + len('def ' + new_func_name)
        args_end_idx = code_solution.find(':\n', args_start_idx)
        full_func = code_solution[func_start_idx : args_end_idx + 2] +'\n    pass\n'

        # parse them out
        argsDec = code_solution[args_start_idx : args_end_idx] + ':\n'
        argsCall = '(' + ', '.join(get_func_args(full_func)) + ')'

        #format the post condition in such a way it can be inserted at the end of the function
        toAdd = '\n'.join(['    ' + line for line in toAdd.split('\n')])
        
        # Now we will be adding a function at the end of the file that
        # is named the same as the entry point and returns the result of
        # the post condition
        wrapper_function = POSTCONDITION_TEMPLATE.substitute(entry_point=entry_point, argsDec=argsDec, argsCall=argsCall, postcondition=toAdd)
        new_solution = code_solution + '\n' +  wrapper_function        

    else:
        raise NotImplementedError
    return new_solution

def paren_check(code):
    """
    Will check if the reason this the code doesn't parse because of a paren error
    """

    try:
        ast.parse(code)

    except Exception as e:
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
        errorMsg = ''.join(tb.msg )
        # remove the paren without a match
        if errorMsg == "unmatched ')'":
            # remove from code the exact paren that is unmatched
            # using the traceback module to get the exact line number and offset
            # of the paren that is unmatched
            code = code.split('\n')
            ln = int(tb.lineno)
            offset = int(tb.offset)
            code[ln - 1] = code[ln - 1][:offset - 2] + code[ln - 1][offset-1:] 
            code = '\n'.join(code)

    return code

def code_sanitize(code: str, numRetries=2) -> str:
    """ 
    This function will sanitize the code to make it more readable, and try to fix basic syntax errors
    """
    
    # First, check if the generated code has syntax errors
    for i in range(numRetries + 1):

        try:
            ast.parse(code)
            
            # If the code compiles, just return it
            return code

        except Exception as e:
            
            # Otherwise, try and fix it -> right now, just does parenthesis errors
            code = paren_check(code)
    
    return None


# simple variable re-namer accounting for basic function scoping
class RenameVariables(ast.NodeTransformer):
    def __init__(self):
        self.var_counter = 0
        self.name_mapping = dict()

    def visit_Name(self, node):
        if node.id not in self.name_mapping:
            self.var_counter += 1
            self.name_mapping[node.id] = f'var{self.var_counter}'
        node.id = self.name_mapping[node.id]
        return node

    def visit_FunctionDef(self, node):
        # Create a new transformer for the new scope
        transformer = RenameVariables()
        # Visit the function body with the new transformer
        node.body = [transformer.visit(n) for n in node.body]
        return node

class duplicateChecker:
    
    def __init__(self):
        
        # This will hold duplicates that are the exact same including comments - only whitespace is stripped
        self.exact_matches = {}
        
        # This will hold versions that we can use to check for lexical code matches 
        # (e.g., comments removed, but variable names remain)
        self.lexical_matches = {}
        
        # This will hold versions of response that we can use to check for a "syntactic match" -> e.g., variable names
        # are abstracted to var1, var2, etc....
        self.syntax_matches = {}
    
        
    def checkAndUpdate(self, newCode, newCodeID):
        
        # Ok, let's do the preprocessing on this sample -> first, let's strip all whitespace
        # except a single ending new line
        charsOnly = ''.join(newCode.split())
        charsOnly = charsOnly.replace('#', '')
        
        codeAst = ast.parse(newCode)
        codeOnly = ast.unparse(codeAst)
        
        varTransform = RenameVariables()
        codeAst = varTransform.visit(codeAst)
        codeAst = ast.fix_missing_locations(codeAst)
        syntaxOnly = ast.unparse(codeAst)
        
        toReturn = {'ExactMatch': None,
                    'LexicalMatch': None,
                    'SyntaxMatch': None
                    }

        # Lookup code in dictionary
        exactId = self.exact_matches.get(charsOnly, None)
        if exactId is not None:
            toReturn['ExactMatch'] = exactId            
        else:
            self.exact_matches[charsOnly] = newCodeID
        
        lexicalId = self.lexical_matches.get(codeOnly, None)
        if lexicalId is not None:
            toReturn['LexicalMatch'] = lexicalId            
        else:
            self.lexical_matches[codeOnly] = newCodeID
        
        syntaxID = self.syntax_matches.get(syntaxOnly, None)
        if syntaxID is not None:
            toReturn['SyntaxMatch'] = syntaxID            
        else:
            self.syntax_matches[syntaxOnly] = newCodeID      
        
        return toReturn    
    
    def summarizeDuplicates(self, logger):
        endL = "\t\t{} unique solutions on the {} level"
        logger("\t🐝 Duplicate summary, there are:")
        logger(endL.format(len(self.exact_matches), 'raw character'))
        logger(endL.format(len(self.lexical_matches), 'lexical code'))
        logger(endL.format(len(self.syntax_matches), 'syntax'))
        
    
def processOneLLMGenFolder(cfg, hydra_cfg, extensionDir=None):
    """
    This file does the processing for one folder specified in the hydraconfig
    """
    #os.chdir(hydra_cfg.runtime.output_dir)
    print_and_log, log_only = log.setup_output_dir(hydra_cfg, extensionDir)
    print_and_log("⚒️  Working directory : {}".format(log.OUTPUT_FOLDER))
    print_and_log(log.make_header("🐈‍⬛  Setting up the output directory  🐈‍⬛"))
    
    print_and_log("Trying to load raw llm samples... ")
    
    # Load the raw data in from the samples_partial llmGen jsonl file
    rawDataFolder = cfg.experiment.samplesFolder
    if extensionDir:
        rawDataFolder = os.path.join(rawDataFolder, extensionDir)
    rawSamplesFile = glob.glob(os.path.join(rawDataFolder, 'samples_partial*'))

    # Check that there is actually one sample file that matches
    if not rawSamplesFile:
        print_and_log("⚠️  Warning: No readable jsonl file in {}, aborting folder".format(rawDataFolder))
        return
    elif len(rawSamplesFile) > 1:
        print_and_log("⚠️  Warning: More than one readable jsonl file {}, aborting folder".format(rawDataFolder))
        return
    
    assert len(rawSamplesFile) == 1
    raw_data = load_jsonl(rawSamplesFile[0])
    print_and_log("😊  Successfully loaded llm-generated code for {} problems".format(len(raw_data)))
    print_and_log("\tCode loaded from: {}".format(rawSamplesFile))
    
    # Copy over the config and raw file and the like from the raw folder
    print_and_log("Now copying raw llm samples and generation meta data... ")
    #oldHydra = os.path.join(rawDataFolder, 'llmGenConfig_HydraCopy')
    #oldHydraCopy = os.path.join(log.OUTPUT_FOLDER, 'llmGenConfig_HydraCopy')
    oldHydra = os.path.join(rawDataFolder, '.hydra')
    oldHydraCopy = os.path.join(log.OUTPUT_FOLDER, 'llmGenConfig_HydraCopy')
    shutil.copytree(oldHydra, oldHydraCopy)
    print_and_log("😊  Successfully copied llm gen hydra from: {} problems".format(oldHydra))
    shutil.copy(rawSamplesFile[0], os.path.join(log.OUTPUT_FOLDER, 'raw_llm_sample_responses.jsonl'))
    print_and_log("😊  Successfully raw samples as reference!!")


    # Load the problem specs
    print_and_log(log.make_header("🐈‍⬛  Loading Benchmark Code 🐈‍⬛"))
    print_and_log("Loading benchmark problems from {}...".format(cfg.benchmarks.name))
    problems = load_benchmarks(cfg.benchmarks)
    print_and_log("😊  Successfully loaded {} problems".format(len(problems)))


    print_and_log(log.make_header("🐈‍⬛  Preprocessing all Samples 🐈‍⬛"))
    # This is the new dictionary that we are building in the format that EvalPlus expects
    new_samples = []

    # For each problem in the data
    last_id = ''
    dupeChecker = duplicateChecker()
    for sample in raw_data:

        task_id = sample['task_id']

        # make sure the choices are sorted by task id
        # Note, this completion_pre seems to be new
        choices = sample['completion_pre']['choices']
        choices.sort(key=lambda x: x['index'])
        canonical_solution = problems[task_id]['prompt'] + problems[task_id]['canonical_solution']

        # If we have moved on to a new problem, reinitialize variables as needed
        if task_id != last_id:
            if last_id != '': dupeChecker.summarizeDuplicates(log_only)
            i = 0
            last_id = task_id
            dupeChecker = duplicateChecker()
        
        # For each model answer for that problem
        for choice in choices:
            rawGen =  choice['message']['content']


            # This removes ```python and ``` wrappings if they exist
            rawGenCode = extract_code(rawGen, cfg.experiment.opensourceModel)
            # This wraps postcondions with the canonical solution
            wrapped = wrap_code_solution(cfg.experiment, canonical_solution, problems[task_id]['entry_point'], rawGenCode)

            # This double checks basic balanced parenthesis with some light fixes
            # returns None if the function has a syntax error
            sanitized = code_sanitize(wrapped)
            
            compiles = True
            
            if not sanitized:
                compiles = False
                sanitized = wrapped
                isDuplicate = None
            else:
            # Finally, check if this sanitized code is a duplicate -> only applicable
            # if this code runs
                isDuplicate = dupeChecker.checkAndUpdate(sanitized, i)       
                
            # Make the new sample in the format required by the EvalPlus
            new_sample = { 
                'task_id': task_id,
                'response_num': i,
                'compiles': compiles,
                'is_duplicate': isDuplicate,
                'solution': sanitized,
                'postcondition_alone': rawGenCode,
                'entry_point': problems[task_id]['entry_point'],
            }

            new_samples.append(new_sample)
            i += 1

            # save this as a human readable file as a byproduct
            program_dir = os.path.join(log.OUTPUT_FOLDER, log.SUB_FOLDER, task_id.replace('/', '_'))
            os.makedirs(program_dir, exist_ok=True)
            
            file_base = task_id.replace('/', '_') + '_' + 'processed_'
            with open(os.path.join(program_dir, file_base + '_' + str(i) + '.py'), 'w') as f:
                f.write(sanitized)

        log_only("\tAdded {} samples for problem {}".format(i, task_id))

    
    print_and_log(log.make_header("🐈‍⬛ Completed Code Preprocessing, Saving jsonl file! 🐈‍⬛"))

    # Write all of the new samples to a file
    outFile = os.path.join(log.OUTPUT_FOLDER, 'preprocessed_samples.jsonl')
    write_jsonl(outFile, new_samples)
    print_and_log(log.make_header("😻 Jsonl Saved to {} 😻".format(outFile)))

@hydra.main(version_base=None, config_path="./config", config_name="config")
def main(cfg):

    # First, get the list of sub folders to see if we are processing a run or a multirun
    rawSamplesFolder = cfg.experiment.samplesFolder
    multirunFile = os.path.join(rawSamplesFolder, 'multirun.yaml')
    hydra_cfg = hydra.core.hydra_config.HydraConfig.get()  

    if os.path.isfile(multirunFile):
        main_log = log.make_print_and_log_function(os.path.join(hydra_cfg.run.dir, "main_log.txt"))
        main_log("🪅  File multirun.yaml exists in the directory:\n{}\nProcessing all folders...".format(rawSamplesFolder))

        for multirunFolder in os.listdir(rawSamplesFolder):
            main_log("\tNow processing subfolder: {}".format(multirunFolder))
            processOneLLMGenFolder(cfg, hydra_cfg, multirunFolder)
        
    else:
        # It is just a basic generation, so we can just do the normal thing:
        processOneLLMGenFolder(cfg, hydra_cfg)
        
if __name__ == "__main__":

    sys.argv.append('hydra.run.dir=response_preprocess_outputs/${now:%Y-%m-%d}/${now:%H-%M-%S}')
    main()
