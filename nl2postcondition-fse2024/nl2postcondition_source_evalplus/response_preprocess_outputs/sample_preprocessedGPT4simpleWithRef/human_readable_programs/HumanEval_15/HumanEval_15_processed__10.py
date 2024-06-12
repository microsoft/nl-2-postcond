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
    
    # Check if the returned string when split by space has the same length as n+1 (as it starts from 0 to n inclusive).
    assert len(return_value.split(" ")) == n + 1
    

    return return_value
