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
    
    # The postcondition checks that if the return value is not None, it is a 32 character long string consisting only of hexadecimal digits
    assert return_value is None or (len(return_value) == 32 and all(c in '0123456789abcdef' for c in return_value))
    

    return return_value
