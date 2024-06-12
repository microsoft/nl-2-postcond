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
    
    # This postcondition checks that if a valid index is returned, the value at that index in the array is less than the value at the preceding index.
    # If the return value is -1, it checks that all elements in the array are in ascending order implying no such index exists.
    assert return_value == -1 if all(arr[i] >= arr[i-1] for i in range(1, len(arr))) else arr[return_value] < arr[return_value - 1]
    

    return return_value
