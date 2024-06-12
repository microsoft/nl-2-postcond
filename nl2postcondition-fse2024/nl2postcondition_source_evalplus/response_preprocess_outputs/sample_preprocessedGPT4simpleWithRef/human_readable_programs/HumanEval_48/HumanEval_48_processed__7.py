def is_palindrome_original(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text == text[::-1]


def is_palindrome(text: str):


    return_value = is_palindrome_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is a boolean (True if the string is a palindrome, False otherwise)
    assert isinstance(return_value, bool), "Return value must be a boolean"
    

    return return_value
