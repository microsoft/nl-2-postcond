def sum_squares_original(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    import math
    return sum(map(lambda x: math.ceil(x) ** 2, lst))


def sum_squares(lst):


    return_value = sum_squares_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Checks if the return value is non-negative. As we square the ceiling of each number, the return value should be non-negative.
    assert return_value >= 0
    

    return return_value
