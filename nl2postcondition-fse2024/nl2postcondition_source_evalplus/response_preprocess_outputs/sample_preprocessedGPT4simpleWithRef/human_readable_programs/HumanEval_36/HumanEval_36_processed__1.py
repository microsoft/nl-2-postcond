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
    
    # The postcondition checks that the return value is an integer and it is non-negative. 
    # This aspect confirms the count nature of the function as it counts the occurrence of a digit and hence, can't be a negative or non-integer value.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
