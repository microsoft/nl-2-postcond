def triangle_area_original(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    p = (a + b + c) / 2
    return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)


def triangle_area(a, b, c):


    return_value = triangle_area_original(a, b, c)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value of the function is -1, when the input sides cannot form a valid triangle.
    # If input sides can form a valid triangle, it checks whether the return value is a non-negative number.
    assert (return_value == -1 and (a + b <= c or a + c <= b or b + c <= a)) or (return_value >= 0 and (a + b > c and a + c > b and b + c > a))
    

    return return_value
