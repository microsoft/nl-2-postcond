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
    
    # The postcondition checks that the return value is greater than or equal to 0 because the sum of ASCII values for uppercase characters can't be negative
    assert return_value >= 0
    

    return return_value
