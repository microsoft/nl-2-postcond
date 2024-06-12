def strange_sort_list_original(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    sorted_list = sorted(lst)
    ans, i, j = ([], 0, len(sorted_list) - 1)
    while i < j:
        ans.append(sorted_list[i])
        ans.append(sorted_list[j])
        i += 1
        j -= 1
    if i == j:
        ans.append(sorted_list[i])
    return ans


def strange_sort_list(lst):


    return_value = strange_sort_list_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the length of the return value is equal to the length of the input list
    assert len(return_value) == len(lst)
    

    return return_value
