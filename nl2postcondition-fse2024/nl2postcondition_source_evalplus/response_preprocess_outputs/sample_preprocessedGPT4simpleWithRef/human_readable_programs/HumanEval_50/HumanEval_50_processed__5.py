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
    
    # This postcondition checks that the decoding process of the function decode_shift is the reverse of the encoding process of the function encode_shift
    assert encode_shift(decode_shift_original(s)) == s
    

    return return_value