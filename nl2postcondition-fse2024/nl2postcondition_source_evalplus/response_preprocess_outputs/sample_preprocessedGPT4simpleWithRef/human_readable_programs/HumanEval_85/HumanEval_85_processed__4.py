def add_original(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    s = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            s += lst[i]
    return s


def add(lst):


    return_value = add_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is an integer. This is due to the fact that the function is expected to return a sum of integers.
    assert isinstance(return_value, int)
    

    return return_value
