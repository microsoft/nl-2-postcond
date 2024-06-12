def solve_original(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    s = sum(map(lambda x: int(x), str(N)))
    return bin(s)[2:]


def solve(N):


    return_value = solve_original(N)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the returned value from the function is a valid binary representation
    # and its integer equivalent is equal to the sum of the decimal digits of the input number N.
    assert int(return_value, 2) == sum(map(int, str(N))), "Return value is not a valid binary representation of the sum of the digits of N."
    

    return return_value
