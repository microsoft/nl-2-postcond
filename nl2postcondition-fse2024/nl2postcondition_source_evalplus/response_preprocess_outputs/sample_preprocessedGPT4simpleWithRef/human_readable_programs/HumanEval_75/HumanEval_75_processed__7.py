def is_multiply_prime_original(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 1:
        return False
    isprime = [True] * (a + 1)
    for i in range(2, a + 1):
        if isprime[i]:
            for j in range(i + i, a + 1, i):
                isprime[j] = False
    cnt, tmp = (0, a)
    for i in range(2, a + 1):
        while isprime[i] and tmp % i == 0:
            tmp //= i
            cnt += 1
    return cnt == 3


def is_multiply_prime(a):


    return_value = is_multiply_prime_original(a)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that if the function returns True,
    # then the product of three prime numbers should be equal to the input 'a'. 
    # If the function returns False, then 'a' should not be a product of exactly three prime numbers.
    # This is done by generating a list of prime numbers up to 'a', 
    # and then checking all combinations of three primes to see if their product equals 'a'.
    
    from itertools import combinations
    from math import prod
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [x for x in range(2, a+1) if is_prime(x)]
    assert (return_value == True and any(prod(comb) == a for comb in combinations(primes, 3))) or \
           (return_value == False and all(prod(comb) != a for comb in combinations(primes, 3)))
    

    return return_value
