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
    
    # The postcondition checks if the returned string is indeed the longest in the list, or None if the list was empty.
    assert return_value is None or len(return_value) == max(len(s) for s in strings)
    

    return return_value
