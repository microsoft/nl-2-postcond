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
    
    # The postcondition checks that the returned list is sorted in ascending order
    # based on the sum of digits of each number. For negative numbers, it considers
    # the absolute value. It does not compare numbers with equal sums of digits,
    # only checks that the sorting is correct where the sums of digits differ.
    assert all(sum(int(digit) for digit in str(abs(a))) <= sum(int(digit) for digit in str(abs(b))) for a, b in zip(return_value, return_value[1:]))
    

    return return_value
