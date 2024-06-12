def common_original(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    return sorted(list(set(l1).intersection(set(l2))))


def common(l1: list, l2: list):


    return_value = common_original(l1, l2)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks whether the returned list is indeed a sorted sequence of unique elements found in both input lists
    assert return_value == sorted([x for x in set(l1) if x in set(l2)])
    

    return return_value
