def sorted_list_sum_original(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    from functools import cmp_to_key

    def cmp(s: str, t: str):
        if len(s) != len(t):
            return len(s) - len(t)
        return -1 if s < t else 1
    return sorted(list(filter(lambda s: len(s) % 2 == 0, lst)), key=cmp_to_key(cmp))


def sorted_list_sum(lst):


    return_value = sorted_list_sum_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the returned list is sorted in ascending order first by the length of the strings and then alphabetically for strings of the same length
    assert return_value == sorted(sorted([x for x in lst if len(x) % 2 == 0], key=len), key=str.lower)
    

    return return_value
