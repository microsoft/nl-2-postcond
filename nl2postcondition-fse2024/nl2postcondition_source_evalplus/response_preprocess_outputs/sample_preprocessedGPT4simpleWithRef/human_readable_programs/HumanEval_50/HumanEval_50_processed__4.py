def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return ''.join([chr((ord(ch) + 5 - ord('a')) % 26 + ord('a')) for ch in s])

def decode_shift_original(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return ''.join([chr((ord(ch) - ord('a') - 5 + 26) % 26 + ord('a')) for ch in s])


def decode_shift(s: str):


    return_value = decode_shift_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the encoded string, when shifted 5 characters back in the alphabet,
    # matches the decoded string returned by the function. This is to verify that the decode_shift function
    # correctly decodes the encoded string.
    assert s == "".join([chr((ord(ch) - ord('a') + 5) % 26 + ord('a')) for ch in return_value])
    

    return return_value
