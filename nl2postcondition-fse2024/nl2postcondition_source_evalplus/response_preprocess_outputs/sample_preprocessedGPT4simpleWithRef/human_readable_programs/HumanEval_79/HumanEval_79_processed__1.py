def decimal_to_binary_original(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    return 'db' + bin(decimal)[2:] + 'db'


def decimal_to_binary(decimal):


    return_value = decimal_to_binary_original(decimal)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Check if the return value is a string, starts and ends with 'db' and contains only 1s and 0s in between.
    assert isinstance(return_value, str) and return_value.startswith('db') and return_value.endswith('db') and all(c in '01' for c in return_value[2:-2]), "Return value must be a string, start and end with 'db' and contain only binary digits in between"
    

    return return_value
