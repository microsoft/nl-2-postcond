from typing import List

def all_prefixes_original(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i + 1] for i in range(len(string))]


def all_prefixes(string: str) -> List[str]:


    return_value = all_prefixes_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the list of prefixes is correctly formatted by checking if each prefix 
    # in the returned list is a prefix of the input string and if the prefixes increase in length.
    assert all(string.startswith(prefix) and len(prefix) == i+1 for i, prefix in enumerate(return_value))
    

    return return_value
