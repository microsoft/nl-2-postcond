import math

def minSubArraySum_original(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if all((x >= 0 for x in nums)):
        return min(nums)
    s, ans = (0, 0)
    for x in nums:
        s += x
        ans = min(ans, s)
        if s >= 0:
            s = 0
    return ans


def minSubArraySum(nums):


    return_value = minSubArraySum_original(nums)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: The return value should be less than or equal to the sum of all elements in the input list, 
    # as it represents the minimum sum of any non-empty sub-array of nums.
    assert return_value <= sum(nums)
    

    return return_value
