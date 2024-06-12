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
    
    # This postcondition checks that the return value is None if the input array is empty, 
    # and that the return value is 0 if the input array contains a 0. 
    assert (arr == [] and return_value is None) or (0 in arr and return_value == 0) or (arr != [] and 0 not in arr)
    

    return return_value
