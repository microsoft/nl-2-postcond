def can_arrange_original(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    for i in range(len(arr) - 1, 0, -1):
        if not arr[i] >= arr[i - 1]:
            return i
    return -1


def can_arrange(arr):


    return_value = can_arrange_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks whether the returned index points to an element in the array which is not greater than or equal to the element immediately preceding it. If the return value is -1, it checks if the array is sorted in ascending order.
    assert return_value == -1 if sorted(arr) == arr else arr[return_value] < arr[return_value - 1]
    

    return return_value
