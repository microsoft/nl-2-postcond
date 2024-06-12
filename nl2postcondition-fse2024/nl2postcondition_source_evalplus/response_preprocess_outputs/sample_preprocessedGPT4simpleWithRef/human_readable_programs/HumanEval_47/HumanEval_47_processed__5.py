def median_original(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_l = sorted(l)
    if len(l) % 2 == 1:
        return sorted_l[len(l) // 2]
    else:
        return (sorted_l[len(l) // 2 - 1] + sorted_l[len(l) // 2]) / 2


def median(l: list):


    return_value = median_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the returned median value is within the range of the list's minimum and maximum values.
    assert min(l) <= return_value <= max(l), "Return value is not within the range of the list's values"
    

    return return_value
