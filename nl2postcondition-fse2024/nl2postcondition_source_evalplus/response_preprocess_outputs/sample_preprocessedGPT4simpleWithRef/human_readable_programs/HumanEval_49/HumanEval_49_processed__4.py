def modp_original(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    res, x = (1, 2)
    while n != 0:
        if n % 2 == 1:
            res = res * x % p
        x = x * x % p
        n //= 2
    return res % p


def modp(n: int, p: int):


    return_value = modp_original(n, p)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the computed value correctly follows the modulo operation property
    # where the return value should be less than the modulo divisor (parameter p in this case)
    assert 0 <= return_value < p, "Postcondition failed: The return value is not within the appropriate range for a modulo operation"
    

    return return_value
