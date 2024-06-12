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
    
    # This postcondition checks if all elements in return_value exist in both l1 and l2, and are unique
    assert all(return_value.count(i) == 1 and i in l1 and i in l2 for i in return_value)
    

    return return_value
