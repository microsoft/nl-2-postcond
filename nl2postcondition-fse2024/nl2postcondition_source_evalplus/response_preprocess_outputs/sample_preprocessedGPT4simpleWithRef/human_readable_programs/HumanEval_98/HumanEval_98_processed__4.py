def count_upper_original(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    cnt = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            cnt += 1
    return cnt


def count_upper(s):


    return_value = count_upper_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is non-negative integer, as the count of uppercase vowels can't be negative
    assert isinstance(return_value, int) and return_value >= 0, "Return value must be a non-negative integer"
    

    return return_value
