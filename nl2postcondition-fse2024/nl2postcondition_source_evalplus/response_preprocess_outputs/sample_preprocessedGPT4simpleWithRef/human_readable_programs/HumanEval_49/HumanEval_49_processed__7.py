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
    
    # The postcondition checks that the returned value is indeed the remainder of (2 to the power of n) divided by p
    assert return_value == (2**n) % p
    

    return return_value
