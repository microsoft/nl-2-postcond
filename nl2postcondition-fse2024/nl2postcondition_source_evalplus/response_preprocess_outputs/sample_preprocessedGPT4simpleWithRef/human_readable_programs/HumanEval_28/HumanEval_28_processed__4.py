from typing import List

def concatenate_original(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


def concatenate(strings: List[str]) -> str:


    return_value = concatenate_original(strings)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the length of the return_value is equal to the sum of lengths of all strings in the input list.
    assert len(return_value) == sum(map(len, strings))
    

    return return_value
