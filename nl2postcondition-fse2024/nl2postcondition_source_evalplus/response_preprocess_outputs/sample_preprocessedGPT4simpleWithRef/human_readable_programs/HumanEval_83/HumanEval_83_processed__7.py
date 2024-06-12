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
    
    # This postcondition checks the validity of the returned count by verifying if it is either 1 (when n is 1)
    # or a positive multiple of 10, since the count of n-digit positive integers that start or end with 1 is calculated
    # as 18 * 10 ** (n - 2) in all other cases.
    
    assert return_value == 1 or return_value % 10 == 0
    

    return return_value
