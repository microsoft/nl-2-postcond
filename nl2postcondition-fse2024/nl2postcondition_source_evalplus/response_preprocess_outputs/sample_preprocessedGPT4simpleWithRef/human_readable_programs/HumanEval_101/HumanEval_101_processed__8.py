def words_string_original(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    words = s.replace(',', ' ').split()
    return [word for word in words if word != '']


def words_string(s):


    return_value = words_string_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that all elements in the returned list are non-empty strings, 
    # which would result from splitting the input string correctly on the commas and spaces
    assert all(isinstance(word, str) and word != "" for word in return_value), "All elements should be non-empty strings"
    

    return return_value
