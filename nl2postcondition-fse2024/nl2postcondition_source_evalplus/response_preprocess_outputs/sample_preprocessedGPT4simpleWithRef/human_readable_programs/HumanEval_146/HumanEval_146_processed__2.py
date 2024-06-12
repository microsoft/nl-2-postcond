def specialFilter_original(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    ans, odd = (0, ['1', '3', '5', '7', '9'])
    for num in nums:
        if num > 10 and str(num)[0] in odd and (str(num)[-1] in odd):
            ans += 1
    return ans


def specialFilter(nums):


    return_value = specialFilter_original(nums)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the returned value is an integer and it's less than or equal to the length of the input list.
    # This asserts the fact that the function cannot return more elements than those present in the input list and 
    # the returned value must be an integer as it represents a count of certain elements in the list.
    assert isinstance(return_value, int) and return_value <= len(nums)
    

    return return_value
