from typing import List

def filter_by_prefix_original(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return list(filter(lambda x: x.startswith(prefix), strings))


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:


    return_value = filter_by_prefix_original(strings, prefix)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: The returned list should only contain strings that start with the given prefix
    assert all(string.startswith(prefix) for string in return_value)
    

    return return_value
