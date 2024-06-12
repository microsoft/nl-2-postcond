def double_the_difference_original(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    """
    ans = 0
    for num in lst:
        if num % 2 == 1 and num > 0 and ('.' not in str(num)):
            ans += num ** 2
    return ans


def double_the_difference(lst):


    return_value = double_the_difference_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Checks if the return_value is a non-negative number (as sum of squares of positive numbers is always non-negative)
    assert isinstance(return_value, (int, float)) and return_value >= 0
    

    return return_value
