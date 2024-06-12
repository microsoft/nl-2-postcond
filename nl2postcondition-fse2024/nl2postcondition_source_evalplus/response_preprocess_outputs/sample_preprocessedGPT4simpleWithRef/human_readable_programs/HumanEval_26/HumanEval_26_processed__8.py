from typing import List

def remove_duplicates_original(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    num_cnt = dict()
    for number in numbers:
        if number not in num_cnt:
            num_cnt[number] = 0
        num_cnt[number] += 1
    return [number for number in numbers if num_cnt[number] == 1]


def remove_duplicates(numbers: List[int]) -> List[int]:


    return_value = remove_duplicates_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that no element in the return list occurs more than once
    assert all(return_value.count(i) == 1 for i in return_value)
    

    return return_value
