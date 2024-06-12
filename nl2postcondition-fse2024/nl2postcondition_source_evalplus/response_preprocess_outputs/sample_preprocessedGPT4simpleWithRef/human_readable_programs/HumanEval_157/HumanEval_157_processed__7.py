def right_angle_triangle_original(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    return a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2


def right_angle_triangle(a, b, c):


    return_value = right_angle_triangle_original(a, b, c)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # This postcondition checks if the return value of the function is consistent with the property of a right-angled triangle. 
    # According to Pythagorean theorem, in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) 
    # is equal to the sum of the squares of the other two sides.
    # This postcondition checks this property by using the input parameters and the return value from the function.
    
    assert (return_value == True and (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2)) or (return_value == False and not (a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2))
    

    return return_value
