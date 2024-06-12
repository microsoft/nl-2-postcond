def remove_vowels_original(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef
ghijklm")
    'bcdf
ghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return ''.join(list(filter(lambda ch: ch not in 'aeiouAEIOU', text)))


def remove_vowels(text):


    return_value = remove_vowels_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the returned string does not contain any vowels.
    assert all(char not in 'aeiouAEIOU' for char in return_value)
    

    return return_value
