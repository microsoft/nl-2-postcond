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
    
    # This postcondition checks whether the result of the function is boolean as per the specification.
    # If the function is implemented correctly, it should always return a boolean value (True or False).
    # This doesn't verify the logic of the function, but it does ensure the output type is as expected.
    assert isinstance(return_value, bool)
    

    return return_value
