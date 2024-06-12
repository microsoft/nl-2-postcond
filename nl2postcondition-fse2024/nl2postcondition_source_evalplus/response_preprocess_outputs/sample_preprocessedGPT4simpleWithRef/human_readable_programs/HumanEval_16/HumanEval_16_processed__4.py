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
    
    # The postcondition checks if the count of unique characters in the lowercased string is equal to the return value
    assert return_value == len(set(string.lower()))
    

    return return_value
