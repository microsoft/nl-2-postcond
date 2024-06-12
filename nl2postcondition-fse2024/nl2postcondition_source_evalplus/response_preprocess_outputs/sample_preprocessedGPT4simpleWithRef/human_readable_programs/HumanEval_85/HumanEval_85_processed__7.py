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
    
    # This postcondition checks if the return value is an integer and non negative. 
    # As the function add_original() adds up even numbers at odd indices of the input list,
    # the result should always be an integer and non negative, since sum of non-negative numbers can't be negative.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
