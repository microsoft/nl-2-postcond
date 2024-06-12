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
    
    # This postcondition checks if the return value is an even number that is less than or equal to y and greater than or equal to x, or -1 if no such number exists.
    assert (return_value == -1 or (return_value % 2 == 0 and x <= return_value <= y)), "Postcondition failed: the return value is not the highest even number within the range [x, y] inclusive or -1 if no such number exists."
    

    return return_value
