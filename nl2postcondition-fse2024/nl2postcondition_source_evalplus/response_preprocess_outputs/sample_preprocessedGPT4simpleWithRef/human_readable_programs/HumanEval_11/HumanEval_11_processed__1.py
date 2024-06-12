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
    
    # This postcondition checks if the length of the return_value is the same as the length of the input strings a and b.
    # This assertion ensures that the XOR operation has been performed on each pair of bits from the input strings.
    assert len(return_value) == len(a) == len(b), "Length of output is not equal to the length of the input strings"
    

    return return_value
