import os
from hydra.types import RunMode
import time

OUTPUT_FOLDER = ""
SUB_FOLDER = "human_readable_programs"

# Function to write log
def write_log(log_file_path, message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(str(message) + "\n")


# Function to create a print_and_log function with a specific log_file_path
def make_print_and_log_function(log_file_path):
    def print_and_log(message):
        print(message)
        write_log(log_file_path, message)
    return print_and_log

# Function to create a log_only function with a specific log_file_path
def make_log_only_function(log_file_path):
    def log_only(message):
        write_log(log_file_path, message)
    return log_only

def setup_output_dir(output_path_dir, pathExtension=None, subfolder=None):
    """
    Sets up the output directory for the run
    """

    # Make directories
    global OUTPUT_FOLDER
    global SUB_FOLDER
    
    if subfolder is not None:
        SUB_FOLDER = subfolder
    
    if isinstance(output_path_dir, str):
        OUTPUT_FOLDER = output_path_dir
    
    else:
        # In this case, it is a hydra config, not a simple path
        hydra_cfg = output_path_dir
        # If we are running multiple versions of the script -> only used for genllm
        if hydra_cfg.mode == RunMode.MULTIRUN:
            print(OUTPUT_FOLDER)
            print(hydra_cfg.sweep.dir, hydra_cfg.sweep.subdir)
            OUTPUT_FOLDER = os.path.join(hydra_cfg.sweep.dir, hydra_cfg.sweep.subdir)
            print(OUTPUT_FOLDER)
        elif pathExtension:
            # In this case, we are uing a path provided by the user
            OUTPUT_FOLDER = os.path.join(hydra_cfg.run.dir, pathExtension)
        else:
            # This is just the standard vanila case
            OUTPUT_FOLDER = hydra_cfg.run.dir
        
    os.makedirs(os.path.join(OUTPUT_FOLDER, SUB_FOLDER), exist_ok=True)
        

    # return print_and_log function
    return make_print_and_log_function(os.path.join(OUTPUT_FOLDER, 'run_log.txt')), \
        make_log_only_function(os.path.join(OUTPUT_FOLDER, 'run_log.txt'))

def make_header(text: str) -> str:
    """
    Makes a pretty header for pretty printing and logging around the text str
    """
    header = "===================================================="
    if len(text) < len(header):
        spaces = " " * ((len(header) - len(text)) // 2)
    else:
        spaces = ""
    return "\n" + header + "\n" + spaces + text + "\n" + header + "\n"