def search_original(lst):
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    """
    count = dict()
    for num in lst:
        if num not in count:
            count[num] = 0
        count[num] += 1
    ans = -1
    for num, cnt in count.items():
        if cnt >= num:
            ans = max(ans, num)
    return ans


def search(lst):


    return_value = search_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the returned value either equals -1 or its frequency in the list is greater than or equal to the value itself.
    assert return_value == -1 or lst.count(return_value) >= return_value
    

    return return_value
