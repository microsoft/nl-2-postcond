def iscube_original(a):
    """
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """
    a = abs(a)
    return int(round(a ** (1.0 / 3))) ** 3 == a


def iscube(a):


    return_value = iscube_original(a)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the result of the function is consistent with the mathematical definition of a cube number.
    # If the function returns True, the cube root of the absolute value of the input parameter (rounded to the nearest integer) should be an integer.
    # If the function returns False, the cube root of the absolute value of the input parameter (rounded to the nearest integer) should not be an integer.
    assert (return_value and round(abs(a) ** (1. / 3)) ** 3 == abs(a)) or (not return_value and round(abs(a) ** (1. / 3)) ** 3 != abs(a))
    

    return return_value
