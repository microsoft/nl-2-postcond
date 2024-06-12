from typing import List

def rescale_to_unit_original(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    ma, mi = (max(numbers), min(numbers))
    k = 1 / (ma - mi)
    return list(map(lambda x: (x - mi) * k, numbers))


def rescale_to_unit(numbers: List[float]) -> List[float]:


    return_value = rescale_to_unit_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the minimum and maximum values of the returned list are 0 and 1 respectively, as per the function's specification. 
    assert min(return_value) == 0.0 and max(return_value) == 1.0, "The smallest number should become 0 and the largest should become 1"
    

    return return_value
