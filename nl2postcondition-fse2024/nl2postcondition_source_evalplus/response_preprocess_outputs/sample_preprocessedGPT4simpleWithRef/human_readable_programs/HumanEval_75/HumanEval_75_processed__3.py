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
    
    # This postcondition checks if the returned value is a boolean. In other words, it's checking if the function is returning True or False as expected.
    assert isinstance(return_value, bool)
    

    return return_value
