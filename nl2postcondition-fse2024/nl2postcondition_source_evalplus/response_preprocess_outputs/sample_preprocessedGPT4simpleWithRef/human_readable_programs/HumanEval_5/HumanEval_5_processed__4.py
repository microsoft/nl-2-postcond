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
    
    # This postcondition checks that the length of the return_value is twice the length of the input list minus 1. 
    # This is because for every element in the input list, we add the element and a delimiter to the return_value. 
    # Hence, the length of return_value should be twice the length of the input list. 
    # But the last element of the input list is not followed by a delimiter, so we subtract one.
    assert len(return_value) == 2*len(numbers) - 1 if numbers else 0, "The output list length is not as expected."
    

    return return_value
