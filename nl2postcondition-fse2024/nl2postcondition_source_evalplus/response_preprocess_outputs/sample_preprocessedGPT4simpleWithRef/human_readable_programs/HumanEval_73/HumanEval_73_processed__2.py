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
    
    # The postcondition checks that the number of changes required to convert the array into a palindromic array is correct.
    # It does this by comparing the original array and a new array obtained by reversing the original array and 
    # replacing the first 'return_value' number of elements with their counterparts from the original array.
    assert arr == arr[:-return_value-1:-1][:return_value] + arr[return_value:len(arr)-return_value] + arr[:return_value][::-1]
    

    return return_value
