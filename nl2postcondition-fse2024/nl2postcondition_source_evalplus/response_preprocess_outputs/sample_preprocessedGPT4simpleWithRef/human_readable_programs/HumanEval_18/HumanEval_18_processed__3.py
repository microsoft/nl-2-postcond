def how_many_times_original(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    occurences = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):
            occurences += 1
    return occurences


def how_many_times(string: str, substring: str) -> int:


    return_value = how_many_times_original(string, substring)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is less than or equal to the length of the string.
    # This is because the number of occurrences of a substring in a string cannot be more than the length of the string itself. 
    assert return_value <= len(string)
    

    return return_value
