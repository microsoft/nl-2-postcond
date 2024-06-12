def is_prime_original(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        return False
    n_sqrt = 1
    while n_sqrt ** 2 < n:
        n_sqrt += 1
    for i in range(2, min(n_sqrt + 1, n)):
        if n % i == 0:
            return False
    return True


def is_prime(n):


    return_value = is_prime_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the return value is consistent with the definition of a prime number
    # A prime number is a number greater than 1 and has no positive divisors other than 1 and itself
    assert return_value == (n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)))
    

    return return_value
