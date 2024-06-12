def fib_original(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b = (1, 1)
    for _ in range(3, n + 1):
        a, b = (b, a + b)
    return b


def fib(n: int):


    return_value = fib_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks whether the return value is a positive integer as all Fibonacci numbers are positive
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
