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
    
    # This postcondition checks if the flipped characters in the returned string match with their corresponding characters in the original string. If a character is lowercase in the original string, it should be uppercase in the returned string and vice versa. If a character is non-alphabetic, it should remain the same.
    assert all((c.islower() and return_value[i].isupper()) or (c.isupper() and return_value[i].islower()) or (not c.isalpha() and c == return_value[i]) for i, c in enumerate(string))
    

    return return_value
