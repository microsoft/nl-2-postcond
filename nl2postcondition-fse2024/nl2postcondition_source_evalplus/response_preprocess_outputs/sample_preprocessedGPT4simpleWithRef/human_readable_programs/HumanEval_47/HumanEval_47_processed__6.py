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
    
    # The postcondition checks if the returned median is actually an element of the list in case of odd number of elements and the average of two middle elements in case of even number of elements.
    assert return_value in l or ((return_value*2) in [l[i] + l[i+1] for i in range(len(l)-1)])
    

    return return_value
