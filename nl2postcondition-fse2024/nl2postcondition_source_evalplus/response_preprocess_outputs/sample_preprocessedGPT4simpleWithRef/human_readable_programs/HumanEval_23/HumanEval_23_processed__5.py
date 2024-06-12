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
    
    # This postcondition checks if the return value is a non-negative integer as length of a string cannot be negative.
    assert isinstance(return_value, int) and return_value >= 0, "Length of string must be a non-negative integer"
    

    return return_value
