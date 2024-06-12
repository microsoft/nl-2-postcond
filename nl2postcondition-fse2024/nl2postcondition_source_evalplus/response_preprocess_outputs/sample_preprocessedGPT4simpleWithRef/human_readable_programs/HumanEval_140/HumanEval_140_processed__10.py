def fix_spaces_original(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    ans = text
    for i in range(len(text) - 1, 2, -1):
        ans = ans.replace(' ' * i, '-')
    return ans.replace(' ', '_')


def fix_spaces(text):


    return_value = fix_spaces_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    import re
    
    # The postcondition checks if all spaces are replaced by underscores or hyphens, and there are no more than 2 consecutive hyphens in the return_value.
    assert all(map(lambda x: x in ['_', '-'] and len(re.findall('-{3,}', return_value)) == 0, return_value)) or text == return_value
    

    return return_value
