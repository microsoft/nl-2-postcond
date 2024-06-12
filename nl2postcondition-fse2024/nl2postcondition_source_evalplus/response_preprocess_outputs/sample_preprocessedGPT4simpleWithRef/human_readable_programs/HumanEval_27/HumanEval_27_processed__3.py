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
    
    # This postcondition checks whether every character in the returned string is the case-swapped version of the corresponding character in the input string.
    assert all(input_char.swapcase() == return_char for input_char, return_char in zip(string, return_value))
    

    return return_value
