from typing import List, Tuple

def rolling_max_original(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [max(numbers[:i + 1]) for i in range(len(numbers))]


def rolling_max(numbers: List[int]) -> List[int]:


    return_value = rolling_max_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Check if every element in the return_value list is the maximum of all preceding elements in the original list
    assert all(numbers[:i+1][-1] >= max(numbers[:i+1]) for i in range(len(numbers)))
    

    return return_value