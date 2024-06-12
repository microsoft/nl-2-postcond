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
    
    # The postcondition checks if the length of the input string is equal to the returned value
    assert len(string) == return_value, "The returned value should be equal to the length of the input string"
    

    return return_value
