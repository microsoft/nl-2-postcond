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
    
    # This postcondition checks if the number of changes (return_value) is sufficient to make the array a palindrome.
    assert arr[:len(arr) // 2] == arr[:len(arr) // 2 - (0 if len(arr) % 2 == 0 else 1):-1]
    

    return return_value
