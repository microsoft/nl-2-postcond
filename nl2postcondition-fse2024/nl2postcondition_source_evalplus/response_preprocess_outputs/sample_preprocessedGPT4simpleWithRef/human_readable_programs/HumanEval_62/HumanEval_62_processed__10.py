def derivative_original(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * i for i in range(1, len(xs))]


def derivative(xs: list):


    return_value = derivative_original(xs)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the length of the returned list is one less than the length of the input list.
    # This is because the derivative of a polynomial reduces the degree of the polynomial by one.
    assert len(return_value) == len(xs) - 1
    

    return return_value
