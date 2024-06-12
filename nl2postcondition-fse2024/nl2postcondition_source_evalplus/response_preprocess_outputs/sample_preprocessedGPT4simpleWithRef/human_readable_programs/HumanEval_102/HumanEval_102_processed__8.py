def choose_num_original(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if x == y:
        return y if y % 2 == 0 else -1
    return y if y % 2 == 0 else y - 1


def choose_num(x, y):


    return_value = choose_num_original(x, y)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is either -1 (when no even number can be found) or an even number within the range [x, y]
    assert return_value == -1 or (x <= return_value <= y and return_value % 2 == 0)
    

    return return_value
