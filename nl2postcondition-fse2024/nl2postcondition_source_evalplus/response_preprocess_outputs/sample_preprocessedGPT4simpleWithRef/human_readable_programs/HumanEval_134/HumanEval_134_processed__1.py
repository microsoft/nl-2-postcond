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
    
    # The postcondition checks if the last character of the string is a letter and not part of a word (i.e., preceded by a space)
    # if the return value is True. If the return value is False, it checks if the string is empty, ends with a space or the last
    # character is part of a word (i.e., not preceded by a space).
    # This is done using regular expressions (re) to match the patterns.
    import re
    assert (return_value and re.search(r' \w$', txt)) or (not return_value and (txt == '' or re.search(r'\w\w$', txt) or txt[-1] == ' '))
    

    return return_value
