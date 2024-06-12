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
    
    # This postcondition checks if the return value is an integer and is greater than or equal to the input parameter n.
    # It ensures that the sum of numbers from 1 to n is not less than n (since n is part of the sum) and is an integer.
    assert isinstance(return_value, int) and return_value >= n
    

    return return_value
