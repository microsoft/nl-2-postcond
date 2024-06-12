def multiply_original(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    return int(str(a)[-1]) * int(str(b)[-1])


def multiply(a, b):


    return_value = multiply_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # This postcondition checks if the return value of the function is a non-negative integer 
    # (since the product of unit digits of two integers, even if one or both are negative, is always non-negative).
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
