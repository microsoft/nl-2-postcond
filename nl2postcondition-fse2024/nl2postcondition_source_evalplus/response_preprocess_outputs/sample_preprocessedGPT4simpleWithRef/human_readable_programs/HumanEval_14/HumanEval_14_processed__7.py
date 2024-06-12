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
    
    # The postcondition checks that the return value is a list of strings, and each string is a prefix of the input string
    assert all(string.startswith(prefix) for prefix in return_value)
    

    return return_value
