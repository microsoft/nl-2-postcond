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
    
    # This postcondition checks that if the function output is True, then the length of the string is at least 3 and all sets of every three consecutive characters in the string are distinct.
    assert ((return_value == True) == (len(s) >= 3 and all(s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2] for i in range(len(s) - 2))))
    

    return return_value
