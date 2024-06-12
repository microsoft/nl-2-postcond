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
    
    # This postcondition checks if the last digit of the product of the unit digits of a and b is the same as the last digit of return_value
    assert int(str(a)[-1]) * int(str(b)[-1]) % 10 == return_value % 10
    

    return return_value
