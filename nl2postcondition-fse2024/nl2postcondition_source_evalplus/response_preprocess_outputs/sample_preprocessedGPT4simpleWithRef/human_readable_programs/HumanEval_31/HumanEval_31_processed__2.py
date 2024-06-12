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
    
    # Postcondition: Checks if all numbers from 2 to the square root of n (inclusive) 
    # are not divisible by n when return_value is True (which means n is prime). 
    # If return_value is False (n is not a prime), the postcondition will be True regardless.
    
    assert return_value == all(n%i != 0 for i in range(2, int(n**0.5)+1)) if return_value else True
    

    return return_value
