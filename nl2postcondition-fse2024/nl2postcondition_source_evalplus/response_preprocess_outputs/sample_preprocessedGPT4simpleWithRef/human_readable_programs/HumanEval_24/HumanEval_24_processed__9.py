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
    
    # The postcondition checks that the return_value is a divisor of n and it's the largest one
    assert n % return_value == 0 and all(n % i != 0 for i in range(return_value + 1, n))
    

    return return_value
