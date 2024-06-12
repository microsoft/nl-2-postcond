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
    
    # The postcondition asserts that each element of return_value is a prefix of the input string, 
    # and that the lengths of the elements in return_value increment by one from 1 to len(string)
    assert all(return_value[i] == string[:i+1] for i in range(len(return_value)))
    

    return return_value
