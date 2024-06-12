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
    
    # The postcondition checks if the return value is not greater than the length of the input string.
    # This is because, the number of distinct characters in a string can never be more than the length of the string itself.
    assert return_value <= len(string)
    

    return return_value
