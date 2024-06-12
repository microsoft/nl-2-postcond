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
    
    # Check that the length of the returned string is equal to the length of the input string
    assert len(return_value) == len(string), "Length of the returned string should be equal to the length of the input string"
    

    return return_value
