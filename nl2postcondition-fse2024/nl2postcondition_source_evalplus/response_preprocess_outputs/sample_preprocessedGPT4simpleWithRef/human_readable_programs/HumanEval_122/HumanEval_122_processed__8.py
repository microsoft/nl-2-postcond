def add_elements_original(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    def digits(x: int) -> int:
        s = str(x)
        return len(s) - 1 if s[0] == '-' else len(s)
    return sum(filter(lambda x: digits(x) <= 2, arr[:k]))


def add_elements(arr, k):


    return_value = add_elements_original(arr, k)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Checks if the returned sum is either equal to or less than the sum of the first k elements in the array 
    assert return_value <= sum(arr[:k])
    

    return return_value
