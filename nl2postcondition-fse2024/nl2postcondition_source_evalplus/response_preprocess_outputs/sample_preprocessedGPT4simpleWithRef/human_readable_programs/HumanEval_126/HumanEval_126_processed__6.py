def is_sorted_original(lst):
    """
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    """
    count = dict()
    for x in lst:
        if x not in count:
            count[x] = 0
        count[x] += 1
        if count[x] > 2:
            return False
    return lst == sorted(lst)


def is_sorted(lst):


    return_value = is_sorted_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Checks if the return value is a boolean, as the function is supposed to return whether the list is sorted and does not contain more than one duplicate.
    assert isinstance(return_value, bool)
    

    return return_value
