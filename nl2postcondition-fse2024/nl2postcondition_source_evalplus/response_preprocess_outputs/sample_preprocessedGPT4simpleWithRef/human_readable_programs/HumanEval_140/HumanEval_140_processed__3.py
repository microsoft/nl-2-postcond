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
    
    # This postcondition checks if the return_value does not contain any whitespace characters and that it has the same length as the input text.
    assert ' ' not in return_value and len(return_value) == len(text), "Postcondition failed: return_value contains whitespace or its length is different from input text"
    

    return return_value
