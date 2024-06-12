def fizz_buzz_original(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    cnt = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            cnt += len(list(filter(lambda c: c == '7', str(i))))
    return cnt


def fizz_buzz(n: int):


    return_value = fizz_buzz_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Assert that the return value is an integer and is non-negative. This is because the function counts occurrences,
    # and count cannot be negative or a non-integer.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
