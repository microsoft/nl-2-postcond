def sum_to_n_original(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return (n + 1) * n // 2


def sum_to_n(n: int):


    return_value = sum_to_n_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is a triangular number. 
    # A triangular number is the sum of all integers up to a certain one. It's called a triangular number 
    # because it represents a triangle with dots. For example, `6` is a triangular number because it's the sum 
    # of `1 + 2 + 3`. So, for every `n` input in sum_to_n function, the return value should always form a triangular number.
    # This is checked by calculating the inverse of the formula for triangular numbers and asserting that it produces an integer.
    assert ((8*return_value + 1)**0.5 - 1) / 2 == n
    

    return return_value
