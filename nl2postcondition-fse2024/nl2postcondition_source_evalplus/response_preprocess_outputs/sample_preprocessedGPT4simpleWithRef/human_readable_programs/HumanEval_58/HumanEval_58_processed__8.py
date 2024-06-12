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
    
    # The postcondition checks that all elements in the return list are present in both input lists and are sorted in ascending order
    assert all(i in l1 and i in l2 for i in return_value) and return_value == sorted(return_value)
    

    return return_value
