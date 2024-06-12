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
    
    # Postcondition: The postcondition is checking that if the function returned True, 
    # the reversed input string should be equal to the original string. 
    # It also checks that if the function returned False, the reversed input string should not be equal to the original string.
    assert (return_value == True and text == text[::-1]) or (return_value == False and text != text[::-1])
    

    return return_value
