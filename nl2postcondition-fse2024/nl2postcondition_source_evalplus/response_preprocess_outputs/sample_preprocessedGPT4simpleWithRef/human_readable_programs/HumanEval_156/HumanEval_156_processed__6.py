def int_to_mini_roman_original(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    m = ['', 'm']
    c = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']
    x = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    i = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    thousands = m[number // 1000]
    hundreds = c[number % 1000 // 100]
    tens = x[number % 100 // 10]
    ones = i[number % 10]
    return thousands + hundreds + tens + ones


def int_to_mini_roman(number):


    return_value = int_to_mini_roman_original(number)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks whether the returned roman numeral is in lowercase as specified in the function docstring.
    assert return_value.islower(), "The return value is not in lowercase"
    

    return return_value
