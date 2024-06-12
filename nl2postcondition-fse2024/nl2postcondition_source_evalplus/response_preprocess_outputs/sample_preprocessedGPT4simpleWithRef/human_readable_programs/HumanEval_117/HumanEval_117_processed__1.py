def select_words_original(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    ans = []
    for word in s.split(' '):
        if word != '':
            c_cnt = len(list(filter(lambda ch: ch not in 'aeiouAEIOU', word)))
            if c_cnt == n:
                ans.append(word)
    return ans


def select_words(s, n):


    return_value = select_words_original(s, n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the return_value is a subset of words from the original string s and each word in return_value contains exactly n consonants.
    assert all(word in s.split(' ') and len(list(filter(lambda ch: ch not in "aeiouAEIOU", word))) == n for word in return_value), "Postcondition failed"
    

    return return_value
