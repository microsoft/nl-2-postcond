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
    
    # Postcondition: Checks whether the return value is an integer and is non-negative.
    # This is because the length of a string can never be a negative number.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
