from typing import List, Tuple

def sum_product_original(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    s, p = (0, 1)
    for number in numbers:
        s += number
        p *= number
    return (s, p)


def sum_product(numbers: List[int]) -> Tuple[int, int]:


    return_value = sum_product_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the sum of the integers in the list is equal to the first element of the returned tuple
    assert sum(numbers) == return_value[0]
    

    return return_value
