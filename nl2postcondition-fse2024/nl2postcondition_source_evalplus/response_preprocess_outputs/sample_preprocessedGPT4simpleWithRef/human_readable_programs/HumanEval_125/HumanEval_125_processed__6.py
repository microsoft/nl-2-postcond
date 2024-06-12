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
    
    # The postcondition checks if the function correctly splits the input string on whitespace or commas, or counts the number of lower-case letters with odd order in the alphabet
    assert (isinstance(return_value, list) and all(isinstance(item, str) for item in return_value) and ' '.join(return_value) in txt) or (isinstance(return_value, int) and return_value == sum(1 for ch in txt if ch.islower() and (ord(ch) - ord('a')) % 2 == 1))
    

    return return_value
