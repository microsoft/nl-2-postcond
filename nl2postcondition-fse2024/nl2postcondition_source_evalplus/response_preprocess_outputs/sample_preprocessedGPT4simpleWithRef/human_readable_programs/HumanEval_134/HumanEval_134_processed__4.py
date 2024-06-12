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
    
    # Postcondition: Checks if the function correctly identifies whether the last character of the input string is not part of a word (preceded by a space)
    assert (return_value == True and txt[-2] == ' ' and txt[-1].isalpha()) or (return_value == False and (txt[-2] != ' ' or not txt[-1].isalpha())) or (len(txt) == 0 and return_value == False), "Postcondition failed!"
    

    return return_value
