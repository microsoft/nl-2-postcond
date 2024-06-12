FIX = '\nAdd more test cases.\n'

def vowels_count_original(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    if s == '':
        return 0
    cnt = len(list(filter(lambda ch: ch in 'aeiouAEIOU', s)))
    if s[-1] in 'yY':
        cnt += 1
    return cnt


def vowels_count(s):


    return_value = vowels_count_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is greater than or equal to zero and less than or equal to the length of the input string 
    # This is because the count of vowels in a string cannot be negative or greater than the length of the string itself
    assert 0 <= return_value <= len(s)
    

    return return_value