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
    
    # Asserts that the return value is a list and each of its elements is a non-empty string.
    # This is ensuring that the function words_string correctly splits the input string into a list of non-empty strings.
    assert isinstance(return_value, list) and all(isinstance(word, str) and word != "" for word in return_value)
    

    return return_value
