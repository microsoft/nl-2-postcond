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
    
    Python
    # Postcondition: If the function returns True, then the cube root of the absolute value of the input, when rounded to the nearest integer and then cubed, should equal the absolute value of the input. If the function returns False, then the cube root of the absolute value of the input, when rounded to the nearest integer and then cubed, should not equal the absolute value of the input.
    assert (return_value == True and int(round(abs(a) ** (1. / 3))) ** 3 == abs(a)) or (return_value == False and int(round(abs(a) ** (1. / 3))) ** 3 != abs(a))
    

    return return_value
