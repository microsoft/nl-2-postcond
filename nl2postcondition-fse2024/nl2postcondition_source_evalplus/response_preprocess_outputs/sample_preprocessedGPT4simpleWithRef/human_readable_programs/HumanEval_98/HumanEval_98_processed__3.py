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
    
    # Postcondition: The return value is a non-negative integer since it counts the occurrences of uppercase vowels at even indices in the string
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
