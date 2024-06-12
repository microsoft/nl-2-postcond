def sort_array_original(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    from functools import cmp_to_key

    def cmp(x: int, y: int) -> int:
        x1 = len(list(filter(lambda ch: ch == '1', bin(x))))
        y1 = len(list(filter(lambda ch: ch == '1', bin(y))))
        if x1 != y1:
            return x1 - y1
        return x - y
    return sorted(arr, key=cmp_to_key(cmp))


def sort_array(arr):


    return_value = sort_array_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return_value is sorted in ascending order 
    # both by number of ones in their binary representation and decimal value.
    # It asserts that for each pair of consecutive elements, the number of ones in 
    # the binary representation of the first element is less than or equal to that 
    # of the second element, and if they are equal, then the decimal value of the 
    # first element is less than or equal to that of the second element.
    assert all(bin(return_value[i]).count('1') < bin(return_value[i + 1]).count('1') or 
               (bin(return_value[i]).count('1') == bin(return_value[i + 1]).count('1') and 
               return_value[i] <= return_value[i + 1]) for i in range(len(return_value) - 1))
    

    return return_value
