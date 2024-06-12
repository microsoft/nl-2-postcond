def starts_one_ends_original(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    return 18 * 10 ** (n - 2)


def starts_one_ends(n):


    return_value = starts_one_ends_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is a non-negative integer as the function should return a count value, which cannot be negative.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
