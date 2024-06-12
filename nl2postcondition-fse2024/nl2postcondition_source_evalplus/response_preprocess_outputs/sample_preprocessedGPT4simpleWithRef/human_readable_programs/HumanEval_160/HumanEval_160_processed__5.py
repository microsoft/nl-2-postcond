def do_algebra_original(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    exp = ''
    for i in range(len(operator)):
        exp += str(operand[i]) + operator[i]
    exp += str(operand[-1])
    return eval(exp)


def do_algebra(operator, operand):


    return_value = do_algebra_original(operator, operand)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the resultant value is an integer. 
    # As per the function's specification, the inputs are non-negative integers and operations include floor division and exponentiation,
    # the result of these operations on integers would always be an integer.
    assert isinstance(return_value, int)
    

    return return_value
