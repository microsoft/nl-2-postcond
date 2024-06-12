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
    
    # Check that the returned list has no duplicates and contains only elements from the input list
    assert all(return_value.count(i) == 1 for i in return_value) and all(i in l for i in return_value)
    

    return return_value
