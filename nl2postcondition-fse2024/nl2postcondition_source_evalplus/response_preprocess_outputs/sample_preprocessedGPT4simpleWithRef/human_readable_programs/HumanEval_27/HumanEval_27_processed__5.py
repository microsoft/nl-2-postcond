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
    
    # The postcondition checks if the case of each character in the return_value is flipped from the original string
    assert all(s.islower() == r.isupper() and s.isupper() == r.islower() for s, r in zip(string, return_value))
    

    return return_value
