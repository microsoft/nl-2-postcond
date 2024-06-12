def rounded_avg_original(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg)


def rounded_avg(n, m):


    return_value = rounded_avg_original(n, m)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that if n <= m, the returned value is a binary string representation. If n > m, the returned value should be -1.
    assert (n <= m and isinstance(return_value, str) and return_value.startswith('0b')) or (n > m and return_value == -1)
    

    return return_value
