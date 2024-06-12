def is_happy_original(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True


def is_happy(s):


    return_value = is_happy_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that if the function returns True, the input string s must be of length 3 or more and all groups of 3 consecutive characters in s must be distinct. If the function returns False, the string s must be of length less than 3 or there exists at least one group of 3 consecutive characters in s that are not distinct.
    import re
    assert (return_value == True and len(s) >= 3 and all(len(set(s[i:i+3])) == 3 for i in range(len(s) - 2))) or (return_value == False and (len(s) < 3 or any(len(set(s[i:i+3])) != 3 for i in range(len(s) - 2))))
    

    return return_value
