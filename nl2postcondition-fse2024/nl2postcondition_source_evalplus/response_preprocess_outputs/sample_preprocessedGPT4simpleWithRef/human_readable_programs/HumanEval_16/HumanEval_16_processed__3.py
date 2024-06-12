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
    
    # Postcondition: Checks if the return value (number of distinct characters) is less than or equal to the length of the input string 
    assert return_value <= len(string), "Number of distinct characters cannot be more than the length of the string"
    

    return return_value
