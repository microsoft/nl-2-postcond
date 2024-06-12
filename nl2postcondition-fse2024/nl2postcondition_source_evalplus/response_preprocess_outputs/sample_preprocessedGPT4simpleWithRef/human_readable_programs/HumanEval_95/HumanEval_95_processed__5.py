def check_dict_case_original(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    keys = list(dict.keys())
    if keys == []:
        return False
    lower, upper = (True, True)
    for k in keys:
        if type(k) != str:
            lower = upper = False
            break
        if not k.islower():
            lower = False
        if not k.isupper():
            upper = False
    return lower or upper


def check_dict_case(dict):


    return_value = check_dict_case_original(dict)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that if the return value is True, then all keys in the dictionary are either entirely in lowercase or entirely in uppercase.
    assert return_value == True implies (all(key.islower() for key in dict.keys()) or all(key.isupper() for key in dict.keys()))
    

    return return_value