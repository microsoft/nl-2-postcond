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
    
    # This postcondition checks if all elements in the return_value list are unique
    assert len(return_value) == len(set(return_value))
    

    return return_value
