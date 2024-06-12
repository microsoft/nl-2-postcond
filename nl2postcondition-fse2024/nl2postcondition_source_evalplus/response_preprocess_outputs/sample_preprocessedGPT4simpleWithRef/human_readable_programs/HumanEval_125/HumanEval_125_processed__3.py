def split_words_original(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    whitespace = tuple(' \n\r\t')
    if any([x in txt for x in whitespace]):
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    cnt = 0
    for ch in txt:
        if ch.islower() and (ord(ch) - ord('a')) % 2 == 1:
            cnt += 1
    return cnt


def split_words(txt):


    return_value = split_words_original(txt)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that when the input string has whitespaces, the returned value is a list of words split by whitespace.
    # In case of no whitespaces but commas, the returned value is a list of words split by comma.
    # If there are no whitespaces or commas, the returned value is an integer representing the number of lowercase alphabets in the input string whose order in the alphabet is odd.
    assert type(return_value) == list and all(isinstance(i, str) for i in return_value) if ' ' in txt or ',' in txt else isinstance(return_value, int)
    

    return return_value
