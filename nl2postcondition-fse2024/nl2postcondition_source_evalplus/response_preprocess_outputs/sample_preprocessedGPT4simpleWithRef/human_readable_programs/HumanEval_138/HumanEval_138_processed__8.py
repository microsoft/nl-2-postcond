def is_equal_to_sum_even_original(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n >= 8 and n % 2 == 0


def is_equal_to_sum_even(n):


    return_value = is_equal_to_sum_even_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is True only for even numbers greater than or equal to 8, as per the function's specification
    assert (return_value == (n >= 8 and n % 2 == 0)), "The function's return value does not match the expected condition"
    

    return return_value
