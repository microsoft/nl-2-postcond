def file_name_check_original(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    if len(list(filter(lambda ch: ch.isdigit(), file_name))) > 3:
        return 'No'
    f_list = file_name.split('.')
    if len(f_list) != 2:
        return 'No'
    if len(f_list[0]) == 0:
        return 'No'
    if not f_list[0][0].isalpha():
        return 'No'
    if f_list[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'


def file_name_check(file_name):


    return_value = file_name_check_original(file_name)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is 'Yes', then the file name should start with a latin alphabet letter and end with one of ['txt', 'exe', 'dll']
    import re
    assert (return_value == 'Yes') implies (re.match(r'^[a-zA-Z].*\.(txt|exe|dll)$', file_name) is not None), "Postcondition failed"
    

    return return_value
