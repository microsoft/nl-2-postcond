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
    
    # This postcondition checks if all the lowercase characters in the original string are now uppercase in the returned string and all the uppercase characters in the original string are now lowercase in the returned string.
    assert all((c.islower() and return_value[i].isupper()) or (c.isupper() and return_value[i].islower()) or c.isspace() for i, c in enumerate(string))
    

    return return_value
