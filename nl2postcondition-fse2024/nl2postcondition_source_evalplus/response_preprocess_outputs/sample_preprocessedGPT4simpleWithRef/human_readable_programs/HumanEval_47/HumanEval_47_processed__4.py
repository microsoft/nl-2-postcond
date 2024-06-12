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
    
    # The postcondition checks if the return value is indeed a median, meaning that at least half of the numbers in the list are less than or equal to it and at least half of them are greater than or equal to it.
    assert sum(i <= return_value for i in l) >= len(l) // 2 and sum(i >= return_value for i in l) >= len(l) // 2
    

    return return_value
