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
    
    # The postcondition checks if the return value is greater than or equal to 1
    # This is because, for any positive integer n, the count of the numbers of n-digit positive integers
    # that start or end with 1 should be at least 1
    assert return_value >= 1
    

    return return_value
