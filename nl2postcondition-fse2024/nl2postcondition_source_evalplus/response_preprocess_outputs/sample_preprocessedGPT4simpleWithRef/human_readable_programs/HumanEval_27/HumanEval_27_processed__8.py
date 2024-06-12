def flip_case_original(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(map(lambda x: x.swapcase(), string))


def flip_case(string: str) -> str:


    return_value = flip_case_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if every character in the returned string is the opposite case of the corresponding character in the input string.
    assert all(string[i].islower() == return_value[i].isupper() and string[i].isupper() == return_value[i].islower() for i in range(len(string)))
    

    return return_value
