def make_a_pile_original(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    ans, num = ([], n)
    for _ in range(n):
        ans.append(num)
        num += 2
    return ans


def make_a_pile(n):


    return_value = make_a_pile_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return list has 'n' elements and if each consecutive element
    # is 2 greater than the previous one, asserting the correct sequence of stones in each level.
    assert len(return_value) == n and all(return_value[i] == return_value[i - 1] + 2 for i in range(1, n))
    

    return return_value
