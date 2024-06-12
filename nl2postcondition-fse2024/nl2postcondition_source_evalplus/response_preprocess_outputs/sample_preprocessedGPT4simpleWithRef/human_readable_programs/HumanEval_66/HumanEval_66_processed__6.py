def digitSum_original(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum([ord(ch) for ch in s if ch.isupper()])


def digitSum(s):


    return_value = digitSum_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return_value is a non-negative integer. 
    # Since ASCII values of upper-case characters are always positive, the sum should be a non-negative integer.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
