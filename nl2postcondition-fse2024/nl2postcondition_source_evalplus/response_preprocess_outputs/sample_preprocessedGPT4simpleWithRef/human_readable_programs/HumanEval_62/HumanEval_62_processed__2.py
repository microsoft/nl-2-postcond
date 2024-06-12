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
    
    # Check that each value in the returned list is a multiple of its index in the input list
    assert all(return_value[i-1] == i*xs[i] for i in range(1, len(xs)))
    

    return return_value
