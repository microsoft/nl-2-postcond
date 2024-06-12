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
    
    # Check that the alternating min-max ordering is respected in the return_value list
    assert all(return_value[i] <= return_value[i+2] for i in range(0, len(return_value)-2, 2)) and all(return_value[i] >= return_value[i+2] for i in range(1, len(return_value)-2, 2))
    

    return return_value
