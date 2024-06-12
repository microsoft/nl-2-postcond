def fibfib_original(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    a, b, c = (0, 0, 1)
    for _ in range(3, n + 1):
        a, b, c = (b, c, a + b + c)
    return c


def fibfib(n: int):


    return_value = fibfib_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value for n=0, n=1, and n=2 is as per the specification in the docstring.
    assert (n in [0, 1] and return_value == 0) or (n == 2 and return_value == 1) or (n > 2 and return_value > 0)
    

    return return_value