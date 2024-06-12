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
    
    # This postcondition checks if the return value is a boolean as the function is expected to return True if the sides form a right-angle triangle and False otherwise
    assert isinstance(return_value, bool)
    

    return return_value
