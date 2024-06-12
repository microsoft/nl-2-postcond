def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome_original(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[i - 1::-1]


def make_palindrome(string: str) -> str:


    return_value = make_palindrome_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return_value is a palindrome
    assert return_value == return_value[::-1]
    

    return return_value
