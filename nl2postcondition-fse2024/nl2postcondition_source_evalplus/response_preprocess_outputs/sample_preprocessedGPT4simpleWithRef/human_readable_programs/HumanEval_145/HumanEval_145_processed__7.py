def order_by_points_original(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def weight(x):
        x_list = list(str(x))
        if x_list[0] == '-':
            x_list = x_list[1:]
            x_list = list(map(int, x_list))
            x_list[0] = -x_list[0]
        else:
            x_list = list(map(int, x_list))
        return sum(x_list)
    return sorted(nums, key=weight)


def order_by_points(nums):


    return_value = order_by_points_original(nums)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    
    # This postcondition checks that the returned list is sorted in ascending order 
    # according to the sum of the digits of its elements. 
    assert all(sum(int(digit) for digit in str(abs(return_value[i]))) <= sum(int(digit) for digit in str(abs(return_value[i+1]))) for i in range(len(return_value) - 1)), "The list is not sorted in ascending order by the sum of the digits of its elements."
    

    return return_value