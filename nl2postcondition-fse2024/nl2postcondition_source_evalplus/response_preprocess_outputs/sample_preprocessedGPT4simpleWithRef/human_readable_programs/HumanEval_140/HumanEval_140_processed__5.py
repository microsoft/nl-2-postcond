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
    
    # This postcondition checks that the returned string does not contain any spaces and if it contains a dash, it should be surrounded by non-space characters
    assert all(char != ' ' for char in return_value) and all(return_value[i-1] != ' ' and return_value[i+1] != ' ' for i, char in enumerate(return_value) if char == '-')
    

    return return_value
