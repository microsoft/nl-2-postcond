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
    
    # Check that all elements in the return_value list start with the given prefix
    assert all([str.startswith(prefix) for str in return_value])
    

    return return_value
