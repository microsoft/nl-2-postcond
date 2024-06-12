def unique_digits_original(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def judge(x):
        for ch in str(x):
            if int(ch) % 2 == 0:
                return False
        return True
    return sorted(list(filter(judge, x)))


def unique_digits(x):


    return_value = unique_digits_original(x)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # This postcondition checks if all digits in the returned numbers are odd and the numbers are in increasing order
    assert all(int(digit) % 2 != 0 for number in return_value for digit in str(number)) and return_value == sorted(return_value)
    

    return return_value
