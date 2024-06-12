def same_chars_original(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return set(s0) == set(s1)


def same_chars(s0: str, s1: str):


    return_value = same_chars_original(s0, s1)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks whether all characters in s0 are present in s1 and vice versa.
    assert all(char in s1 for char in s0) == return_value and all(char in s0 for char in s1) == return_value
    

    return return_value
