def string_sequence_original(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(map(str, range(n + 1)))


def string_sequence(n: int) -> str:


    return_value = string_sequence_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is a string containing n+1 space-separated elements 
    # and each element is a digit increasing consecutively from 0 to n.
    assert len(return_value.split()) == n + 1 and all(str(i) == element for i, element in enumerate(return_value.split()))
    

    return return_value
