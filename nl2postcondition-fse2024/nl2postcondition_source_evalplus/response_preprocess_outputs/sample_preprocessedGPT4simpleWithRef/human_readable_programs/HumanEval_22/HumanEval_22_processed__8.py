from typing import List, Any

def filter_integers_original(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return list(filter(lambda x: type(x) == int, values))


def filter_integers(values: List[Any]) -> List[int]:


    return_value = filter_integers_original(values)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Checks if all elements in the return_value list are of integer type
    assert all(isinstance(i, int) for i in return_value), "All elements in the return list are not integers"
    

    return return_value
