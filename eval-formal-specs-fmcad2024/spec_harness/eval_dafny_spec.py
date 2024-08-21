
def read_dafny_program(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        dafny_code = "".join(lines)
        return dafny_code

import os
import random
import re
import subprocess

# global variables
max_mutations = None
dafny_binary_path = None
smoke_test = False
user_labels_json = []

def parse_code_blocks(source_code):
    # Define states
    BEGIN_BLOCK, IN_BLOCK, NO_BLOCK = 'BEGIN_BLOCK', 'IN_BLOCK', 'NO_BLOCK'
    state = NO_BLOCK

    # Define keywords and initialize variables
    keywords = ['predicate', 'function', 'method']
    blocks = []
    index = 0
    block_type = []
    block_name = []
    block_prefix = []
    block_body = []
    current_prefix = ''
    current_name = None
    current_body = ''
    current_type = ''
    brace_stack = []

    # Helper function to reset the current block when it ends
    def reset_current_block():
        nonlocal current_type, current_body, current_prefix, state
        block_body.append(current_body)
        #block_type.append(current_type)
        current_body = ''
        current_prefix = ''
        current_name = None
        state = NO_BLOCK

    # Process each character in the source code
    while index < len(source_code):
        char = source_code[index]

        if state == NO_BLOCK:
            # Check if the upcoming substring is a keyword
            for keyword in keywords:
                if source_code[index:].startswith(keyword):
                    state = BEGIN_BLOCK
                    block_type.append(keyword)
                    index += len(keyword)
                    block_prefix.append('')
                    # find the block name as the first word after the keyword
                    b_name = re.search(r'\w+', source_code[index:])
                    current_name = b_name.group(0)  
                    block_name.append(current_name)
                    # increment the index by the length of the block name
                    index += len(current_name)
                    break

        elif state == BEGIN_BLOCK:
            if char == '{':
                brace_stack.append(char)
                state = IN_BLOCK
                current_body += char
            else:
                block_prefix[-1] += char

        elif state == IN_BLOCK:
            current_body += char
            if char == '{':
                brace_stack.append(char)
            elif char == '}':
                brace_stack.pop()
                if not brace_stack:  # End of block detected
                    reset_current_block()
                    continue

        index += 1

    # If the file ends but still in IN_BLOCK state, finalize the last block
    if state == IN_BLOCK and brace_stack == []:
        reset_current_block()

    # Combine prefixes and bodies
    combined_blocks = [{'name' : name, 'type' : type, 'prefix': prefix, 'body': body} for name, type, prefix, body in zip(block_name, block_type, block_prefix, block_body)]

    return combined_blocks

def parse_tests(source_code, callee_name):
    test_cases = []
    current_test = None

    lines = source_code.split('\n')
    for line in lines:
        line = line.strip()
        
        # Detect variable initialization with array assignment
        if line.startswith('var') and ':=' in line:
            if current_test is None:
                current_test = {'inputs': [], 'outputs': []}
            var_name, var_value = line.split(':=')[0].strip(), line.split(':=')[1].strip()
            var_name = var_name.replace('var ', '').strip()
            current_test['inputs'].append((var_name, var_value))

        # Detect expected results in comments
        elif line.startswith('//expected'):
            expected_result = line.replace('//expected', '').strip().strip(';').strip()
            current_test['outputs'].append(expected_result)
            test_cases.append(current_test)
            current_test = None

        # Detect assert statement for output
        elif line.startswith('assert') or line.startswith('//assert') or line.startswith('expect'):
            output_value = line.split('==')[1].strip().strip(';').strip()
            current_test['outputs'].append(output_value)
            test_cases.append(current_test)
            current_test = None

        # Detect method call and expected result
        if callee_name in line:
            result_assignment, method_call = line.split(':=')
            current_test['method_call'] = callee_name

    return test_cases

# a wrapper around process_example that checks for exceptions
def process_example(dafny_file_path_prefix):

    try:
        user_label = None
        if not (user_labels_json  == []):
            # find out the user-label for this example
            # find the suffix id of dafny_file_path_prefix by splitting on "task_id_<id>"
            suffix = (dafny_file_path_prefix.split("task_id_")[1]).strip()
            print (f"{dafny_file_path_prefix} Suffix: {suffix}")
            # find user label by looking for "suffix" in "id" field and reading the "note" field
            user_label = next(label["note"] for label in user_labels_json if label["id"] == suffix)
            # strip any newlines for printing
            user_label = user_label.replace("\n", "").strip()

        (avg_correct_stats, avg_complete_stats) = process_example_aux(dafny_file_path_prefix)
        # print these stats
        print(f"{dafny_file_path_prefix} Average Correctness: {avg_correct_stats}, Average Completeness: {avg_complete_stats}, User label: {user_label}\n---")
    except Exception as e:
        print (f"{dafny_file_path_prefix} Error processing file")
        print (e)

        

def process_example_aux(dafny_file_path_prefix):
    dafny_file_path = dafny_file_path_prefix + ".dfy"
    print(f"Processing file: {dafny_file_path}")
    dafny_code = read_dafny_program(dafny_file_path)
    # Parse the code
    parsed_blocks = parse_code_blocks(dafny_code)
    for block in parsed_blocks:
        print(f"Name: {block['name']}")
        print(f"Type: {block['type']}")
        print(f"Prefix:\n{block['prefix']}")
        print(f"Body:\n{block['body']}\n---")

    # find the name of the block being invoked in block named 'Main'
    main_block = next(block for block in parsed_blocks if block['name'] == 'Main')
    invoked_block_name = re.search(r'\w+', main_block['body']).group(0)
    print (f"Block being invoked in Main: {invoked_block_name}")

    #find the block being invoked in the main block
    invoked_block = next(block for block in parsed_blocks if block['name'] == invoked_block_name)

    # find the body of the invoked block
    invoked_block_body = invoked_block['body']

    # remove "Test" suffix from the invoked block name
    invoked_block_name = invoked_block_name.replace("Test", "")

    # correctness stats 
    correct_stats = 0
    complete_stats = 0

    tests = parse_tests(invoked_block_body, invoked_block_name)    
    for i, test in enumerate(tests):
        # create an outcome for each test and mutants
        outcomes = []
        print(f"Inputs: {test['inputs']}")
        print(f"Method Call: {test['method_call']}")
        print(f"Expected Output: {test['outputs']}\n---")
        tmp = generate_dafny_test_harness(test, parsed_blocks, dafny_file_path_prefix)
        outcomes.append((-1, tmp))
        # generate some mutations of the test harness
        for i in range(max_mutations):
            tmp = generate_dafny_test_harness(test, parsed_blocks, dafny_file_path_prefix, mutate=True)
            outcomes.append((i, tmp))
        # print only the 2nd component of each outcome
        print(f"{dafny_file_path_prefix} Outcomes: {[(i, res) for (i, (a, res, b)) in outcomes]}\n---")
        # print a stripped version where we only look for # of errors in the string
        # look for a regex ".*Dafny program verifier finished with \d+ verified, \d+ error.*"
        # first get the compressed outcomes using the regex on 2nd component of each outcome
        compressed_outcomes = [re.search(r'.*Dafny program verifier finished with (\d+) verified, (\d+) error.*', res, re.DOTALL) for (i, (a, res, b)) in outcomes]
        # then get the number of errors from the compressed outcomes
        errors = [int(x.group(2)) for x in compressed_outcomes]
        print(f"{dafny_file_path_prefix} Dafny Statistics for test: {errors}\n---")
        # update correct and complete stats
        correct_stats += 1 if errors[0] == 0 else 0
        # check number of incorrect mutations as number of 1s in errors[1:]
        complete_stats += errors[1:].count(1)
    avg_correct_stats = correct_stats/len(tests)
    avg_complete_stats = complete_stats/(len(tests)*max_mutations)
    return (avg_correct_stats, avg_complete_stats)

def mutate_value(input_value, mutate):
    if not mutate:
        return input_value
    # if mutation is enabled, then mutate the input randomly

    print (f"mutating input_value: {input_value}")
    if input_value.isdigit():
        val = int(input_value)
        # randomly choose a positive integer and randomly add or subtract it
        random_val = random.randint(1, 10)
        if random.choice([True, False]):
            input_value = str(val + random_val)
        else:
            input_value = str(val - random_val)
     # if the input is a boolean, then negate it
    elif input_value == "true":
        input_value = "false"
    elif input_value == "false":
        input_value = "true"
    elif input_value.startswith("new int[]"):
        # if the input is an array, then do one of the following:
        # add a random element to a random position of the array
        # remove a element at a random position from the array
        # assert ensure that its an array of integers

        # remove the "new int[]" from the input_value
        input_value = input_value.replace("new int[]", "")
        # mutate the array value
        input_value = mutate_array_value(input_value)
        # add "new int[]" back to the input_value
        input_value = "new int[]" + input_value
    elif input_value.startswith("["): # seq of integers
        input_value = mutate_array_value(input_value)
    else:
        # replace any " " in the string
        input_value = input_value.replace('"', '')
        print (f"entering mutating alnum value with {input_value}")
        # if the input is a alphanumeric string, then add a character to it
        # choose a random character to add or remove from input_value
        random_char = random.choice("abcdefghijklmnopqrstuvwxyz")
        random_pos = random.randint(0, len(input_value)+1)
        if random_pos == len(input_value) + 1:
            input_value = input_value + random_char
        else:
            input_value = input_value[:random_pos] + random_char + input_value[random_pos:]
        input_value = f"\"{input_value}\""
    print (f"mutated input_value: {input_value}")

    return input_value

def mutate_array_value(input_value):
    # remove the "[" and "]" from the input_value
    input_value = input_value.replace("[", "").replace("]", "")
    # parse input_value to get the array of integers
    input_value = [int(x) for x in input_value.split(",")]
    # randomly choose a position to add or remove an element
    random_pos = random.randint(0, len(input_value)-1)
    # randomly choose a value to add to the array
    random_val = random.randint(0, 100)
    if random.choice([True, False]):
        # add the random_val to the array at random_pos
        input_value.insert(random_pos, random_val)
    else:
        # remove the element at random_pos
        input_value.pop(random_pos)
    # convert the input_value back to the string
    return "[" + ",".join([str(x) for x in input_value]) + "]"

def generate_dafny_test_harness(test, parsed_blocks, dafny_file_path, mutate=False):
    """
    Generate a test harness for the given test case and parsed blocks
    Really hacky string/regex processing, but it works for now except array equality
    """

    # find all non-method blocks
    non_method_blocks = [block for block in parsed_blocks if block['type'] != 'method']
    # inline these blocks in the test harness
    test_harness_code = ""  
    for block in non_method_blocks:
        test_harness_code += f"{block['type']} {block['name']} {block['prefix']}\n{block['body']}\n"

    callee_block = next(block for block in parsed_blocks if block['name'] == test['method_call'])
    # callee_block_body = callee_block['body']
    test_harness_code += f"method {callee_block['name']} {callee_block['prefix']}{{\n"

    # parse the arguments and return from prefix of the block
    prefix = callee_block['prefix']
    params = re.search(r'\((.*?)\)', prefix).group(1)
    params = params.split(',')
    for param in params:
        test_harness_code += f"  //param {param.strip()};\n"
    out_params = re.search(r'.*returns\s*\((.*?)\)', prefix).group(1)
    # we only handle a single output for now
    assert out_params.count(',') == 0, "Multiple outputs not supported"
    for out_param in out_params.split(','):
        test_harness_code += f"  //out_param {out_param};\n"
    
    for input_var, input_value in test['inputs'][:-1]:
        # don't mutate inputs, only outputs
        test_harness_code += f"  var {input_var} := {input_value}\n"
    test_harness_code += f"  //var {test['inputs'][-1][0]} := {test['inputs'][-1][1]};\n"

    # parse the arguments and returns from the last line of test['inputs']
    ret_params = test['inputs'][-1][0]
    ret_params = ret_params.split(',')
    for ret_param in ret_params:
        test_harness_code += f"  //ret_args {ret_param.strip()};\n"
    
    # parse input_value from the last line of test['inputs']
    input_value = test['inputs'][-1][1]
    # parse the args 
    args = re.search(r'\((.*?)\)', input_value).group(1)
    args = args.split(',')
    for arg in args:
        test_harness_code += f"  //arg {arg.strip()};\n"

    #test_harness_code += f"  assert false;\n"

    # create a zip of params and args
    for param1, arg, inp in zip(params, args, test['inputs']):
        print (f"param: {param1}, arg: {arg}")
        # strip the type from x: type from params
        param = param1.split(':')[0]
        # check if the arg is an array
        type = param1.split(':')[1].strip()
        # check if type contains the regex pattern array<\w+>
        if re.search(r'array<\w+>', type):
            # if it does, then we need to convert arg to sequence
            param2 = param 
            param = param + f"[..{param}.Length]"
            arg2 = arg
            arg = arg + f"[..{arg}.Length]"  
            # cannot compare arrays as they are references
            # so need to compare each element of the array
            test_harness_code += f"  //need to equate the elements of the array, and not reference (which is inconsistent)\n"
            test_harness_code += f"  assume {{:axiom}} {param.strip()} == {arg.strip()};\n"

            # extract the size of the array by looking for number of "," in the arg
            size = inp[1].count(",") + 1
            # need to add redundant asserts to make dafny happy by iterating over all elements of the array
            # explicitly add the equality of the elements upto the size
            test_harness_code += f"  //redundant asserts to make dafny happy\n"
            for i in range(size):
                test_harness_code += f"  assert {param2.strip()}[{i}] == {arg2.strip()}[{i}];\n"
        else:
            test_harness_code += f"  assume {{:axiom}} {param.strip()} == {arg.strip()};\n"


    # create a zip of out_params and test['outputs']
    out_param = out_params.split(',')[0].split(':')[0]
    ret_value = test['outputs'][0] # assuming a single output for now
    # add "new int[]" to the out_param if the type of the out_param is array and ret_param has no "new int[]"
    print (f"out_params: {out_params}, ret_value: {ret_value}")
    if re.search(r'array<int>', out_params):
        if not "new int[]" in ret_value:
            ret_value = "new int[]" + ret_value 

    ret_value = mutate_value(ret_value, mutate)
    test_harness_code += f"  {out_param.strip()} := {ret_value.strip()};\n"
    if smoke_test:
        test_harness_code += f"  assert false;\n"

    test_harness_code += f"  //var expectedOutput := {ret_param};\n"
    test_harness_code += f"}}"
    print("\n------------\nTest Harness Code:\n-----------------")
    print(test_harness_code)
    # create an output file wiht dafny_file_path + "_test_harness.dfy"
    with open(dafny_file_path + "_test_harness.dfy", "w") as file:
        file.write(test_harness_code)

    # invoke dafny on the test harness file with argument "verify"
    result = subprocess.run([dafny_binary_path,  "verify", "--allow-warnings", dafny_file_path + "_test_harness.dfy"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

    return (test_harness_code, result.stdout, result.stderr)

# add command line arguments to the harness
import argparse
import sys
import json

def init_parser():
    parser = argparse.ArgumentParser(description='Check a Dafny specification for test-set correctness and completeness for user-intent formalization.')
    parser.add_argument('--file', type=str, help='path to the dafny file without the .dfy extension')
    # add a flag to mutate the inputs and number of mutations (default 5)
    parser.add_argument('--mutate', type=int, default=5, help='number of mutations to apply to each test')
    # log file to store the results
    parser.add_argument('--log', type=str, help='path to the log file')
    # path to Dafny binary
    parser.add_argument('--dafny-binary', type=str, default="/home/shuvendu/dafny/Scripts/dafny",  help='path to the Dafny binary')
    # smoke test to check if assert false is reachable
    parser.add_argument('--smoke-test', action='store_true', help='smoke test to check if assert false is reachable')
    # a json file with user labels
    parser.add_argument('--user-labels-json', type=str, help='path to the json file with user labels')
    return parser

# Example usage
if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()
    log_file = args.log
    if args.dafny_binary:
        print (f"Using Dafny binary: {args.dafny_binary}")
        dafny_binary_path = args.dafny_binary

    # redirect the output to the log file
    if log_file:
        print (f"Redirecting output to {log_file}")
        sys.stdout = open(log_file, 'w')

    # set the mutation flag
    max_mutations = args.mutate

    # smoke test to check if assert false is reachable
    if args.smoke_test:
        smoke_test = True

    if args.user_labels_json:
        # read the json file
        with open(args.user_labels_json, "r") as file:
            user_labels_json = json.load(file)
            
    # if the file argument is provided, then process the file
    if args.file:
        # ensure that the file exists and has no extension
        assert os.path.exists(args.file+".dfy"), "File does not exist"
        process_example(args.file)    
    else:
        # hardcode some examples for testing
        process_example("examples/task_id_2") # first 
        process_example("examples/task_id_2_fixed") # <==> instead of ==>
        process_example("examples/task_id_101") # assert for expected output
        process_example("examples/task_id_594") # //assert for expected output
        process_example("examples/task_id_433") # truea/falsea
        process_example("examples/task_id_447") # truea/falsea
        process_example("examples/task_id_105") # recursive function needs {: fuel} annotation. DOES NOT WORK yet




