def special_factorial_original(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fac, ans = (1, 1)
    for i in range(2, n + 1):
        fac *= i
        ans *= fac
    return ans


def special_factorial(n):


    return_value = special_factorial_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return value is greater than or equal to the input value, 
    # since the special factorial of a number should always be greater than or equal to the number itself.
    assert return_value >= n
    

    return return_value
