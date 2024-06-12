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
    
    # This postcondition checks whether the return value is a positive integer (or zero) as all Fibonacci numbers are.
    # By definition, Fibonacci sequence starts with 0 and 1 and every subsequent number is the sum of two preceding ones.
    # This guarantees that all Fibonacci numbers are non-negative.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
