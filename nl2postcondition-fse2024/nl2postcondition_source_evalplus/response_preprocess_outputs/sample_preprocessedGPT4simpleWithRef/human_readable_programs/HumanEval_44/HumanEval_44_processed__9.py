def change_base_original(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    ret = ''
    while x != 0:
        ret = str(x % base) + ret
        x //= base
    return ret


def change_base(x: int, base: int):


    return_value = change_base_original(x, base)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the returned string, when converted back to the original base, equals the original number
    assert int(return_value, base) == x
    

    return return_value
