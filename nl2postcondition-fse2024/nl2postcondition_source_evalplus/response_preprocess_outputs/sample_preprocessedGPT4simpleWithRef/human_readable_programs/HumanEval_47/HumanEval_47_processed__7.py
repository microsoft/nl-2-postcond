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
    
    # Postcondition: The return_value is either in the list l itself if the list length is odd, or the average of two values in the list if the list length is even.
    assert return_value in l or (return_value * 2 in [l[i] + l[i+1] for i in range(len(l)-1)])
    

    return return_value
