from typing import List

def factorize_original(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        fact.append(n)
    return fact


def factorize(n: int) -> List[int]:


    return_value = factorize_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    # The postcondition checks whether the product of all factors in the return_value matches the original input number n
    assert n == eval('*'.join(map(str, return_value))), 'The product of factors does not match the original number'

    return return_value
