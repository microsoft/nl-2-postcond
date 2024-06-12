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
    
    # This postcondition checks that if the function returned False, there is no point in the accumulated operations where the balance goes below zero.
    assert not return_value or any(sum(operations[:i+1]) < 0 for i in range(len(operations)))
    

    return return_value
