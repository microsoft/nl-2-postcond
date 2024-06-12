from typing import List

def intersperse_original(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    res = []
    for i in range(len(numbers)):
        res.append(numbers[i])
        if i != len(numbers) - 1:
            res.append(delimeter)
    return res


def intersperse(numbers: List[int], delimeter: int) -> List[int]:


    return_value = intersperse_original(numbers, delimeter)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the length of the returned list is equal to twice the length of the input list minus 1. 
    # This is because for every number in the input list, there should be a corresponding number and delimiter in the output list, except for the last number which does not have a subsequent delimiter.
    assert len(return_value) == 2 * len(numbers) - 1 if numbers else 0
    

    return return_value
