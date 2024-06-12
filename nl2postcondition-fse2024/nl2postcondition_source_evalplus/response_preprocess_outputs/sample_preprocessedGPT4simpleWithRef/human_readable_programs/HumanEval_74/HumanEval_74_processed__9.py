def total_match_original(lst1, lst2):
    """
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    """
    c1, c2 = (sum(map(lambda s: len(s), lst1)), sum(map(lambda s: len(s), lst2)))
    return lst1 if c1 <= c2 else lst2


def total_match(lst1, lst2):


    return_value = total_match_original(lst1, lst2)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the total number of characters in all strings of the returned list
    # is less than or equal to the total number of characters in all strings of the non-returned list.
    assert sum(map(len, return_value)) <= sum(map(len, lst1 if return_value != lst1 else lst2))
    

    return return_value
