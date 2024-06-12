def smallest_change_original(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    arr_reversed, cnt = (arr[::-1], 0)
    for i in range(len(arr) // 2):
        if arr[i] != arr_reversed[i]:
            cnt += 1
    return cnt


def smallest_change(arr):


    return_value = smallest_change_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the number of elements that need to be changed (return_value) 
    # and the actual number of differences between the first half and reversed second half of the array are equal
    assert return_value == sum(el1 != el2 for el1, el2 in zip(arr, arr[::-1])[:len(arr)//2])
    

    return return_value
