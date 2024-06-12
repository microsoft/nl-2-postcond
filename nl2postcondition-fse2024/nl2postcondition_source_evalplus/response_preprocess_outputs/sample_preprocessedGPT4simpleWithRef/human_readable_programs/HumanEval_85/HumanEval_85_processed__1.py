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
    
    # The postcondition checks if the returned value is an integer, and it is equal to or greater than zero. 
    # This is because the function is adding even numbers which are always positive or zero, 
    # and the returned value should reflect this behavior.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
