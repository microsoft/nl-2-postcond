def reverse_delete_original(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    ss = ''.join(filter(lambda ch: ch not in c, s))
    return (ss, ss == ss[::-1])


def reverse_delete(s, c):


    return_value = reverse_delete_original(s, c)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the first element of the return tuple, when reversed, is equal to itself if and only if the second element of the return tuple is True. 
    assert return_value[1] == (return_value[0] == return_value[0][::-1])
    

    return return_value
