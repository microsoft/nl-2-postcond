def next_smallest_original(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if len(lst) <= 1:
        return None
    sorted_list = sorted(lst)
    for x in sorted_list:
        if x != sorted_list[0]:
            return x


def next_smallest(lst):


    return_value = next_smallest_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the returned value is the second smallest element in the list 
    # or None if there is no such element
    assert return_value == None or (lst.count(return_value) == lst.count(min(set(lst), key=lst.count)) and return_value > min(lst))
    

    return return_value
