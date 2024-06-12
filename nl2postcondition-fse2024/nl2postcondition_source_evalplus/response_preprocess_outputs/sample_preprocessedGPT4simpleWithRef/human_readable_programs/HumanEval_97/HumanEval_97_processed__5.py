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
    
    # This postcondition checks if the return value is the product of the units digit of both input parameters.
    assert return_value == (a % 10) * (b % 10)
    

    return return_value
