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
    
    # This postcondition checks that the length of the return value is correct. If there are n elements in the input list, 
    # the return list should have 2n-1 elements because a delimeter is added between every two elements. 
    # For an empty list, the result is also an empty list.
    assert len(return_value) == 2 * len(numbers) - 1 if numbers else 0
    

    return return_value
