def prime_fib_original(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import random

    def miller_rabin(n, k=10):
        """Test if n is prime using the Miller-Rabin primality test."""
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        r = 0
        d = n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    c_prime = 0
    a, b = (0, 1)
    while c_prime < n:
        a, b = (b, a + b)
        if miller_rabin(b):
            c_prime += 1
    return b


def prime_fib(n: int):


    return_value = prime_fib_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the function has returned a prime number
    # It uses a simple method to check for primality: a number is prime if it has no divisors other than 1 and itself
    assert all(return_value % i for i in range(2, int(return_value**0.5) + 1)) and return_value > 1
    

    return return_value
