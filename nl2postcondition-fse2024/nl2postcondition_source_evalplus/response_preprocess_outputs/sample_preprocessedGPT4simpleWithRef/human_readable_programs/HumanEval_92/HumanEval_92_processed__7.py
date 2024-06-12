def any_int_original(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    """
    if type(x) != int or type(y) != int or type(z) != int:
        return False
    return x == y + z or y == x + z or z == y + x


def any_int(x, y, z):


    return_value = any_int_original(x, y, z)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is False when any of the inputs is not an integer. 
    # This is based on the specification that all numbers should be integers for the function to return True.
    assert return_value or not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int))
    

    return return_value
