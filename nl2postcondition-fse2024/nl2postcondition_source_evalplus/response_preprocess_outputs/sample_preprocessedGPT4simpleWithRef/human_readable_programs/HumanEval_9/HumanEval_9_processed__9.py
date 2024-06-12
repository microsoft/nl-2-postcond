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
    
    # Check if the return_value list has the same length as the input list, and each element of return_value 
    # is the maximum of the corresponding subsequence in the input list.
    assert len(return_value) == len(numbers) and all(return_value[i] == max(numbers[:i+1]) for i in range(len(numbers)))
    

    return return_value
