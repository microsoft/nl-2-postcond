def check_if_last_char_is_a_letter_original(txt):
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    """
    if len(txt) == 0:
        return False
    if len(txt) == 1:
        return txt.isalpha()
    return txt[-1].isalpha() and txt[-2] == ' '


def check_if_last_char_is_a_letter(txt):


    return_value = check_if_last_char_is_a_letter_original(txt)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the function correctly handles empty strings and strings ending with a space.
    # As per the function specification, if the input string is empty or ends with a space, the function should return False.
    # The postcondition asserts this behavior using the strip() method to remove trailing spaces from the input string and
    # then checks if the return value is False when the stripped string is empty.
    assert not (txt.strip() == '' and return_value)
    

    return return_value
