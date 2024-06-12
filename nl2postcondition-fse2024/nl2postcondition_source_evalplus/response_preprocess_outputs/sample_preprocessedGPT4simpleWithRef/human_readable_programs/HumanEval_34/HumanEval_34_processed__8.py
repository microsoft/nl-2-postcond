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
    
    # This postcondition checks that the returned list is sorted in ascending order. 
    # It does this by comparing each element to the next one and ensuring that the current element is less than or equal to the next one.
    assert all(return_value[i] <= return_value[i + 1] for i in range(len(return_value) - 1))
    

    return return_value
