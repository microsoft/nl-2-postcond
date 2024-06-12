def prod_signs_original(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if arr == []:
        return None
    if 0 in arr:
        return 0
    s, sgn = (0, 1)
    for x in arr:
        s += abs(x)
        sgn *= x // abs(x)
    return s * sgn


def prod_signs(arr):


    return_value = prod_signs_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the returned value is None when the input list is empty
    assert (return_value is None) == (len(arr) == 0)
    

    return return_value
