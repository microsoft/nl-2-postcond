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
    
    # Postcondition: The return value should be equal to the length of a list comprehension that 
    # iterates through the string and checks if the substring starts at each index, counting overlapping occurrences.
    assert return_value == len([i for i in range(len(string)) if string[i:].startswith(substring)])
    

    return return_value
