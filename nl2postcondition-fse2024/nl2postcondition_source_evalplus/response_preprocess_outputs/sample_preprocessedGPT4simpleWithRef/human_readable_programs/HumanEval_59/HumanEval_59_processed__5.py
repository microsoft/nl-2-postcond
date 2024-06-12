def largest_prime_factor_original(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    isprime = [True] * (n + 1)
    for i in range(2, n + 1):
        if isprime[i]:
            for j in range(i + i, n, i):
                isprime[j] = False
    for i in range(n - 1, 0, -1):
        if isprime[i] and n % i == 0:
            return i


def largest_prime_factor(n: int):


    return_value = largest_prime_factor_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is a prime number and it is a factor of input n
    assert return_value > 1 and all(return_value % i != 0 for i in range(2, int(return_value ** 0.5) + 1)) and n % return_value == 0
    

    return return_value