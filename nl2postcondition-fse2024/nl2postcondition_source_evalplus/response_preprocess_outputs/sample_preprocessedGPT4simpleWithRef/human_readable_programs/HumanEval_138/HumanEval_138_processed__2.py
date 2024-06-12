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
    
    # This postcondition checks whether the return value is False when n is smaller than 8 or not even,
    # which would make it impossible to be written as the sum of exactly 4 positive even numbers
    assert return_value == False if n < 8 or n % 2 != 0 else True
    

    return return_value
