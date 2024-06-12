from typing import List

def string_xor_original(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return ''.join((str(int(a[i]) ^ int(b[i])) for i in range(len(a))))


def string_xor(a: str, b: str) -> str:


    return_value = string_xor_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the length of the return_value is equal to the length of input strings a and b.
    # Since XOR operation is performed on each character of the input strings, the result should have the same length.
    assert len(return_value) == len(a) == len(b), "Output length should be equal to the input lengths"
    

    return return_value
