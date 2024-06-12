from typing import List

def below_zero_original(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    account = 0
    for operation in operations:
        account += operation
        if account < 0:
            return True
    return False


def below_zero(operations: List[int]) -> bool:


    return_value = below_zero_original(operations)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the return value is True if there exists a cumulative sum of operations that is negative.
    # It uses the Python built-in functions `any` and `sum` to check all possible cumulative sums.
    assert return_value == any(sum(operations[:i+1]) < 0 for i in range(len(operations)))
    

    return return_value
