def string_to_md5_original(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == '':
        return None
    import hashlib
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()


def string_to_md5(text):


    return_value = string_to_md5_original(text)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the function returns None when the input is an empty string and if the function returns a string of length 32 when the input is not an empty string
    assert (text == "" and return_value is None) or (text != "" and isinstance(return_value, str) and len(return_value) == 32)
    

    return return_value