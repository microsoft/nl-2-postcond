def greatest_common_divisor_original(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    def query_gcd(a: int, b: int) -> int:
        return a if b == 0 else query_gcd(b, a % b)
    return query_gcd(a, b)


def greatest_common_divisor(a: int, b: int) -> int:


    return_value = greatest_common_divisor_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return_value divides both input integers without a remainder.
    assert a % return_value == 0 and b % return_value == 0
    

    return return_value
