# a driver to invoke eval_dafny_spec.py on all the .dfy files in a folder
# and report the results

# usage: python3 eval_dafny_spec_folder.py folder
# command line arguments:

import argparse

parser = argparse.ArgumentParser(description='Evaluate Dafny specs in a folder')
parser.add_argument('--folder', type=str, help='folder containing .dfy files')

# path to a user-labels-json file
parser.add_argument('--user-labels-json', type=str, help='path to a user-labels-json file')

# --user-labels-json ~/dafny-synthesis/RQs/RQ3-\[Dynamic-Few-Shot-Prompting\]/rq3-dynamic-few-shot-prompting-GPT-4-temp_0.5-verified-unverified-tagged.json

def process_folder(folderPath, user_labels_json_file):
    import os
    import subprocess
    import sys

    # get the list of .dfy files in the folder
    files = [f for f in os.listdir(folderPath) if f.endswith('.dfy')]

    # remove any file of the form "*_test_harness.dfy"
    files = [f for f in files if '_test_harness.dfy' not in f]

    # create a unique string with date and time
    import datetime
    now = datetime.datetime.now()
    # converto a string 
    now_str = "dmp_" + now.strftime('%Y_%m_%d_%H_%M_%S')
    # create a folder with the current date and time in current folder
    os.mkdir(now_str)

    # call eval_dafny_spec on each file
    for file in files:
        #strip the extension from the file name
        file = file[:-4]
        fullpath = folderPath + '/' + file
        dafny_binary = '/home/shuvendu/dafny/Scripts/dafny'
        # create a logfile  in now_str folder
        log_file = now_str + '/' + file + '.dmp.txt'
        print('Processing file', fullpath)
        subprocess.run(
            ['python3', 'eval_dafny_spec.py', 
             '--dafny', dafny_binary, 
             '--mutate', '5', 
             '--file', fullpath,
             '--log', log_file,
             '--user-labels-json', user_labels_json_file             
            ])

def main():
    args = parser.parse_args()
    folderPath = args.folder
    user_labels_json_file = args.user_labels_json
    process_folder(folderPath, user_labels_json_file)

if __name__ == '__main__':
    main()

