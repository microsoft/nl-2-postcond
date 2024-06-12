from typing import List, Optional

def longest_original(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    maxlen = max((len(x) for x in strings))
    for s in strings:
        if len(s) == maxlen:
            return s


def longest(strings: List[str]) -> Optional[str]:


    return_value = longest_original(strings)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that if the function returned a value, then the length of this value is greater than or equal to the length of every string in the input list
    assert return_value is None or all(len(return_value) >= len(s) for s in strings)
    

    return return_value
