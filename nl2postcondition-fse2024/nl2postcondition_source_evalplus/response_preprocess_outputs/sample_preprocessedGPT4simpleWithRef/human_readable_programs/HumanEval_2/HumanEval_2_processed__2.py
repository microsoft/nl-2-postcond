def truncate_number_original(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)


def truncate_number(number: float) -> float:


    return_value = truncate_number_original(number)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is a float and lies in the range [0, 1). It verifies that the function correctly returns the decimal part of the number.
    assert isinstance(return_value, float) and 0 <= return_value < 1
    

    return return_value
