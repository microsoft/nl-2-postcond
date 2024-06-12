def count_distinct_characters_original(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.lower()))


def count_distinct_characters(string: str) -> int:


    return_value = count_distinct_characters_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the returned value is an integer and it's less than or equal to the length of the input string. 
    # This is because the number of distinct characters in a string cannot be more than the length of the string itself, and it must be an integer.
    assert isinstance(return_value, int) and return_value <= len(string), "Return value must be an integer and less than or equal to the length of the string"
    

    return return_value
