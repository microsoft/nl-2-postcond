def skjkasdkd_original(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """

    def is_prime(a):
        return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))
    sorted_list = sorted(lst)[::-1]
    for x in sorted_list:
        if is_prime(x):
            return sum(map(lambda ch: int(ch), str(x)))


def skjkasdkd(lst):


    return_value = skjkasdkd_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is an integer and if it is greater than or equal to zero.
    # This is because the sum of digits of a largest prime number in the list will always be an integer and non-negative.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
