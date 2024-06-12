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
    
    # The postcondition checks that decoding the encoded string gives back the original string
    assert encode_shift(return_value) == s
    

    return return_value
