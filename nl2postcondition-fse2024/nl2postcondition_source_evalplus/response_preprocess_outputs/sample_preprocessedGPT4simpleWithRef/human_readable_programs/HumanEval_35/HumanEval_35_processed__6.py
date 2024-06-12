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
    
    # Postcondition: The return value should be greater than or equal to every element in the input list
    assert all(return_value >= x for x in l), "Return value is not the maximum element in the list"
    

    return return_value