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
    
    # The postcondition checks that the return value is non-negative and is less than or equal to half the length of the input string.
    # This captures the fact that we're only checking even indices, and that each character can contribute at most 1 to the count.
    assert 0 <= return_value <= len(s) // 2
    

    return return_value
