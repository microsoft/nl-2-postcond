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
    
    # Postcondition: Checks if the return value is less than 1.0 and greater or equal to 0.0
    assert 0.0 <= return_value < 1.0, "Return value should be a decimal part of the number"
    

    return return_value
