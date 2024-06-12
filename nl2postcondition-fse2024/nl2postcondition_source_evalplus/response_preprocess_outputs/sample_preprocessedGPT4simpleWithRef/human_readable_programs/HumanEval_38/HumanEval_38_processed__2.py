def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[1:] + group[0] if len(group) == 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic_original(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[3 * i:min(3 * i + 3, len(s))] for i in range((len(s) + 2) // 3)]
    groups = [group[2] + group[:2] if len(group) == 3 else group for group in groups]
    return ''.join(groups)


def decode_cyclic(s: str):


    return_value = decode_cyclic_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the length of the return_value is equal to the length of the input string. 
    # This confirms that no characters were added or removed during the decoding process.
    assert len(return_value) == len(s), "The length of the decoded string does not match the length of the input string"
    

    return return_value
