def even_odd_palindrome_original(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    odd_cnt, even_cnt = (0, 0)
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 1:
                odd_cnt += 1
            else:
                even_cnt += 1
    return (even_cnt, odd_cnt)


def even_odd_palindrome(n):


    return_value = even_odd_palindrome_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the number of even and odd integer palindromes within the given range (1 to n) are as expected.
    # It does so by recreating the list of palindromes and verifying that the counts match the returned values.
    assert (sum(1 for i in range(1, n + 1) if str(i) == str(i)[::-1] and i % 2 == 0), 
            sum(1 for i in range(1, n + 1) if str(i) == str(i)[::-1] and i % 2 == 1)) == return_value
    

    return return_value
