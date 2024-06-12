def get_positive_original(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return list(filter(lambda x: x > 0, l))


def get_positive(l: list):


    return_value = get_positive_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that all numbers in the returned list are positive
    assert all(i > 0 for i in return_value), "All elements should be positive"
    

    return return_value
