def digits_original(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    has_odd, prod = (False, 1)
    for ch in str(n):
        if int(ch) % 2 == 1:
            has_odd = True
            prod *= int(ch)
    return 0 if not has_odd else prod


def digits(n):


    return_value = digits_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Check if the return value is 0 when all digits in the input number are even
    assert (return_value == 0) == all(int(digit) % 2 == 0 for digit in str(n))
    

    return return_value
