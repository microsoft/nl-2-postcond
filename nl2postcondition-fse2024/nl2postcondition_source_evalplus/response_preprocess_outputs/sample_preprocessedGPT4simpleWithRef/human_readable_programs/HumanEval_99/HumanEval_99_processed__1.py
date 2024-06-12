def closest_integer_original(value):
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    """

    def rounding(val):
        if abs(val - int(val)) != 0.5:
            return round(val)
        if val > 0:
            return int(val) + 1
        else:
            return int(val) - 1
    return rounding(float(value))


def closest_integer(value):


    return_value = closest_integer_original(value)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the returned value is an integer and its difference from the float input is less than or equal to 0.5. 
    # This ensures that the function is rounding to the closest integer. 
    # It also checks if the rounding is done away from zero in case of a tie.
    assert isinstance(return_value, int) and abs(float(value) - return_value) <= 0.5 and (float(value) - return_value <= 0 if abs(float(value) - int(float(value))) == 0.5 else True)
    

    return return_value
