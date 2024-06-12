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
    
    # The postcondition checks if the returned string from remove_vowels function does not contain any vowels
    assert all(ch not in "aeiouAEIOU" for ch in return_value)
    

    return return_value