def sort_array_original(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if array == []:
        return []
    return sorted(array, reverse=(array[0] + array[-1]) % 2 == 0)


def sort_array(array):


    return_value = sort_array_original(array)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the returned list is sorted in the correct order based on the sum of the first and last elements of the input list
    assert (return_value == sorted(array) and (array[0]+array[-1])%2 == 1) or (return_value == sorted(array, reverse=True) and (array[0]+array[-1])%2 == 0)
    

    return return_value
