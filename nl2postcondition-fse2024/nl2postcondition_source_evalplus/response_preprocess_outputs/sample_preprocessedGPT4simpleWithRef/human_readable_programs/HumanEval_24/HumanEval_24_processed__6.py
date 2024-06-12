def largest_divisor_original(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(2, n):
        if n % i == 0:
            return n // i
    return 1


def largest_divisor(n: int) -> int:


    return_value = largest_divisor_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Checks if the return value is indeed a divisor of the input number n and also smaller than n.
    assert n % return_value == 0 and return_value < n
    

    return return_value
