def incr_list_original(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]


def incr_list(l: list):


    return_value = incr_list_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Checks that the length of the returned list is same as the input list
    assert len(l) == len(return_value), "The length of the returned list should be same as that of the input list"
    

    return return_value
