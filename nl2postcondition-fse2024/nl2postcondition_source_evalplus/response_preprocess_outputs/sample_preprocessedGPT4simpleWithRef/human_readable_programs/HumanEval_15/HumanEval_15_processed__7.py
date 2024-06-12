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
    
    # Check that the returned string, when split by spaces, gives a list of length n+1 
    # (since it should include numbers from 0 to n inclusive)
    assert len(return_value.split(" ")) == n + 1
    

    return return_value
