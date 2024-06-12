def strlen_original(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def strlen(string: str) -> int:


    return_value = strlen_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return value is a non-negative integer, which is expected from a length function
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
