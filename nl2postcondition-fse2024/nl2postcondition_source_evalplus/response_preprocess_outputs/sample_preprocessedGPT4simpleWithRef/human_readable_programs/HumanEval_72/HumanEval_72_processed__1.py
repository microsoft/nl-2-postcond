def will_it_fly_original(q, w):
    """
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    """
    return q == q[::-1] and sum(q) <= w


def will_it_fly(q, w):


    return_value = will_it_fly_original(q, w)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that if the function returns True, then the sum of elements in the input list is less than or equal to the maximum possible weight.
    assert (return_value == True) implies (sum(q) <= w)
    

    return return_value
