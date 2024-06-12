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
    
    # This postcondition checks if the returned value from the function is either a list of words or a number.
    # If it's a list, it checks that all elements in the list are strings and have no whitespaces or commas inside them.
    # If it's an integer, it checks that it's non-negative since it represents a count.
    # The postcondition doesn't check that the function correctly identifies words, commas, or lower case letters with odd order,
    # but it provides a sanity check on the type and format of the returned value.
    
    import re
    
    assert isinstance(return_value, list) and all(isinstance(word, str) and not re.search(r'\s|,', word) for word in return_value) or (isinstance(return_value, int) and return_value >= 0)
    

    return return_value
