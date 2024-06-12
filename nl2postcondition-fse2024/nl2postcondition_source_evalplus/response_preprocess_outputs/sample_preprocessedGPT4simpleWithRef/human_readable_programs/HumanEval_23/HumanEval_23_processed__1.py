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
    
    # The postcondition checks that the returned value is a non-negative integer, as the length of a string cannot be a negative number.
    assert isinstance(return_value, int) and return_value >= 0, "The returned value must be a non-negative integer"
    

    return return_value
