def circular_shift_original(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    shift %= len(s)
    if shift == 0:
        return s
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


def circular_shift(x, shift):


    return_value = circular_shift_original(x, shift)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the length of the return_value is equal to the length of the input number
    assert len(str(x)) == len(return_value)
    

    return return_value
