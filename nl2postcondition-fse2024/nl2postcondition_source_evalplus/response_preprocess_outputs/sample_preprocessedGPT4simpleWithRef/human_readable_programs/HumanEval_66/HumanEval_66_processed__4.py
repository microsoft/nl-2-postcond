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
    
    # Postcondition: Checks if the return value is a positive integer value or zero as it's the sum of ASCII codes of the upper characters in the input string
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
