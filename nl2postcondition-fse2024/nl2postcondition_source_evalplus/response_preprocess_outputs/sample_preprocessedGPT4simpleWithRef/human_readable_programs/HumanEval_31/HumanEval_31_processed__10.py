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
    
    # The postcondition checks whether the return value is consistent with the definition of a prime number.
    # A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
    # So, if the return value is True, then for any number in the range from 2 to n-1, n should not be divisible by that number.
    # If the return value is False, then there should exist at least one number in the range from 2 to n-1, by which n is divisible.
    assert (return_value and all(n % i for i in range(2, n))) or (not return_value and any(n % i == 0 for i in range(2, n)))
    

    return return_value
