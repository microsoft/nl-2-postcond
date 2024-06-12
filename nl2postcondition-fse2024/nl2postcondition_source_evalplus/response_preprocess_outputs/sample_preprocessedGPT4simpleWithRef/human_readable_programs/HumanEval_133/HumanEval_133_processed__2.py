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
    
    # The postcondition checks that the return value is greater than or equal to the sum of the list elements. 
    # This is because squaring a number and taking the ceiling always makes it larger or leaves it the same.
    assert return_value >= sum(lst)
    

    return return_value
