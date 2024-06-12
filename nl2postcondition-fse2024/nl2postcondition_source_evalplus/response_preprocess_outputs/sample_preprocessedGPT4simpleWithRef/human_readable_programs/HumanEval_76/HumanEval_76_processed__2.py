def is_simple_power_original(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if x == 1:
        return True
    if n == 0:
        return x == 0
    if n == 1:
        return x == 1
    if n == -1:
        return abs(x) == 1
    p = n
    while abs(p) <= abs(x):
        if p == x:
            return True
        p = p * n
    return False


def is_simple_power(x, n):


    return_value = is_simple_power_original(x, n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return_value is boolean since the function is expected to return either True or False
    assert isinstance(return_value, bool)
    

    return return_value
