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
    
    # Postcondition: If the function returns True, then there must have been at least one operation
    #                that made the cumulative sum of operations till that point negative.
    #                If the function returns False, then the cumulative sum of operations was always non-negative.
    assert (return_value == True and any(sum(operations[:i+1]) < 0 for i in range(len(operations)))) or (return_value == False and all(sum(operations[:i+1]) >= 0 for i in range(len(operations))))
    

    return return_value
