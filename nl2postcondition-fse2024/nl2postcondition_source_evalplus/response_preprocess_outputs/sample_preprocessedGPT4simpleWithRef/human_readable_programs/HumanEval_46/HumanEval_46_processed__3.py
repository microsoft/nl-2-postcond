def fib4_original(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = (0, 0, 2, 0)
        for i in range(4, n + 1):
            a, b, c, d = (b, c, d, a + b + c + d)
        return d


def fib4(n: int):


    return_value = fib4_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is non-negative and an integer. This is because the fib4 sequence is defined as a sum of previous integers and it always starts with non-negative integers.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
