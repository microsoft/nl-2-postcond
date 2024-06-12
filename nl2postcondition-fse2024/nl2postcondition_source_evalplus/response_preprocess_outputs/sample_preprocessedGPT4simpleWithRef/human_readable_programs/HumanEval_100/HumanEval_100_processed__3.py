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
    
    # The postcondition checks if the number of elements in the return list is equal to the input number n
    # and if the last element in the return list is equal to 2n-1 if n is odd, or 2n if n is even.
    # This captures the function's behavior of creating a pile with n levels, 
    # where the number of stones in each level is an odd number if n is odd, and even number if n is even.
    
    assert len(return_value) == n and return_value[-1] == (2*n if n%2 == 0 else (2*n - 1)), "Postcondition failed!"
    

    return return_value
