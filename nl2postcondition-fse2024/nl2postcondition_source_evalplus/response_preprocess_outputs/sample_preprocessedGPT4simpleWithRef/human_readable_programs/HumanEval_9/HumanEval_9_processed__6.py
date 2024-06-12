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
    
    # This postcondition checks that the last element of the return_value list is the maximum of the original input list
    assert return_value[-1] == max(numbers), "The last element of the return list is not the maximum of the input list"
    

    return return_value
