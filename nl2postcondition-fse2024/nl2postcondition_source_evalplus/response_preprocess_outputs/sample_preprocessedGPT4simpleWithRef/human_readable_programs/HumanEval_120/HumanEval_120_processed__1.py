def maximum_original(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    return sorted(sorted(arr)[::-1][:k])


def maximum(arr, k):


    return_value = maximum_original(arr, k)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the return value is a sorted list with length equal to k
    assert len(return_value) == k and all(return_value[i] <= return_value[i + 1] for i in range(len(return_value) - 1))
    

    return return_value
