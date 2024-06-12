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
    
    # The postcondition checks that every element in the return_value list appears only once, 
    # indicating that the function has correctly returned unique elements from the input list.
    assert all(return_value.count(x) == 1 for x in return_value)
    

    return return_value
