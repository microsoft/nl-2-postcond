def max_element_original(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    assert all((type(x) in [int, float] for x in l)), 'invalid inputs'
    return max(l)


def max_element(l: list):


    return_value = max_element_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the return value is indeed an element in the input list and is greater than or equal to every other element in the list.
    assert return_value in l and all(return_value >= x for x in l), "Return value is not the maximum element in the list"
    

    return return_value
