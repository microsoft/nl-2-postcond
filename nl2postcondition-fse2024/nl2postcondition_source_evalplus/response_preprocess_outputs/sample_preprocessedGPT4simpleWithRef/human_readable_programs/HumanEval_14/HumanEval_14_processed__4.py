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
    
    # The postcondition checks if each element of the return_value list is a prefix of the input string and 
    # if the length of each prefix in the return_value list is equal to its index plus one.
    assert all(return_value[i] == string[:i+1] for i in range(len(return_value)))
    

    return return_value
