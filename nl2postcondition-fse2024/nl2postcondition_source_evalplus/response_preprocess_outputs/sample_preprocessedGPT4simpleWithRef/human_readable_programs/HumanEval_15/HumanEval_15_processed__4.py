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
    
    # The postcondition checks that the return_value is a string of space-separated numbers from 0 to n inclusive.
    assert return_value == ' '.join(str(i) for i in range(n+1))
    

    return return_value
