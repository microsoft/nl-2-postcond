def encrypt_original(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    d = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(map(lambda ch: chr((ord(ch) - ord('a') + 4) % 26 + ord('a')) if ch in d else ch, s))


def encrypt(s):


    return_value = encrypt_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Check if the returned string has the same length with the input string.
    # This asserts that the encryption process did not add or remove any characters.
    assert len(s) == len(return_value)
    

    return return_value