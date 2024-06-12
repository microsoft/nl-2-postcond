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
    
    # This postcondition checks whether all lowercase characters in the input string have been turned to uppercase in the return value and vice versa.
    assert all(x.lower() == y if x.isupper() else x.upper() == y for x, y in zip(string, return_value))
    

    return return_value
