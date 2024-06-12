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
    
    # Postcondition: Checks if the return_value is sorted in ascending order when the sum of first and last elements of the input array is odd, else it checks if its sorted in descending order. Also, checks that the length of return_value is equal to the length of input array.
    assert (return_value == sorted(array) if sum([array[0], array[-1]]) % 2 else return_value == sorted(array, reverse=True)) and len(return_value) == len(array)
    

    return return_value
