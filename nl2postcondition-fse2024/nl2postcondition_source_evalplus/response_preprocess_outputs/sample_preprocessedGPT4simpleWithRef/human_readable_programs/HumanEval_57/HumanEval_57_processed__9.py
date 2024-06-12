def monotonic_original(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    inc, dec = (True, True)
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            inc = False
        if l[i] < l[i + 1]:
            dec = False
    return inc or dec


def monotonic(l: list):


    return_value = monotonic_original(l)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Checks if the list is either consistently increasing or decreasing when the function returns True
    assert return_value == (all(l[i] <= l[i+1] for i in range(len(l)-1)) or all(l[i] >= l[i+1] for i in range(len(l)-1)))
    

    return return_value
