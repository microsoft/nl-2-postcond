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
    
    # The postcondition checks if the return value is equal to the number of start indices of the substring in the original string.
    # It uses a list comprehension to generate a list of Booleans, each of which represents whether the string starting at that index starts with the substring.
    # The all() function is then used to check if all values in the list are True.
    # If the number of Trues is equal to the return value, it means that the function has correctly counted the number of occurrences of the substring in the string, including overlaps.
    assert return_value == sum([1 for i in range(len(string)) if string[i:].startswith(substring)])
    

    return return_value
