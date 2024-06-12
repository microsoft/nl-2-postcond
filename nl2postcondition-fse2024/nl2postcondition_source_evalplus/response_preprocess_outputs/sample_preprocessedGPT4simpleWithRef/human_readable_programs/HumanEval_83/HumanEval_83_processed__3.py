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
    
    # Check if the return value is positive, as the count of numbers should always be non-negative. Also, it should be less than or equal to the total number of n-digit integers possible.
    assert 0 <= return_value <= 10**n
    

    return return_value
