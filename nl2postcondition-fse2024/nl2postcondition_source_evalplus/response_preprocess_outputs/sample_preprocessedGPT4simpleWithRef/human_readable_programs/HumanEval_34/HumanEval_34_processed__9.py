def unique_original(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))


def unique(l: list):


    return_value = unique_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return_value is in ascending order and all elements in return_value are unique
    assert all(return_value[i] < return_value[i+1] for i in range(len(return_value)-1)) and len(set(return_value)) == len(return_value)
    

    return return_value
