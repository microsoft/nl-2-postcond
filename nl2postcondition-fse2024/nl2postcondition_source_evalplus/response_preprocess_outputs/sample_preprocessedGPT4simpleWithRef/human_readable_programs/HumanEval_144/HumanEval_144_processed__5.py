def simplify_original(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    x1, x2 = map(int, x.split('/'))
    n1, n2 = map(int, n.split('/'))
    return x1 * n1 % (x2 * n2) == 0


def simplify(x, n):


    return_value = simplify_original(x, n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is a boolean, as the specification mentions that the function should return True or False.
    assert isinstance(return_value, bool), "Return value must be a boolean"
    

    return return_value
