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
    
    # The postcondition checks if the length of the returned list is equal to the input integer 'n' 
    # and if the difference between successive elements in the list is 2 which ensures that the list is 
    # following the pattern of increasing by the next even or odd number.
    assert len(return_value) == n and all(return_value[i+1] - return_value[i] == 2 for i in range(n-1))
    

    return return_value