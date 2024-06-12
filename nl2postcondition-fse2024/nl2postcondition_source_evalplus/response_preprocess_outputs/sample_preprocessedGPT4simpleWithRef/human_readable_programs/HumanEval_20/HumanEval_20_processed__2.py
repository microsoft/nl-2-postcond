from typing import List, Tuple

def find_closest_elements_original(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    min_diff = float('inf')
    min_pair = None
    for l, r in zip(numbers[:-1], numbers[1:]):
        diff = r - l
        if diff < min_diff:
            min_diff = diff
            min_pair = (l, r)
    return min_pair


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:


    return_value = find_closest_elements_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the returned pair of numbers are in the original list and the second number is greater or equal to the first one
    assert return_value[0] in numbers and return_value[1] in numbers and return_value[0] <= return_value[1]
    

    return return_value
