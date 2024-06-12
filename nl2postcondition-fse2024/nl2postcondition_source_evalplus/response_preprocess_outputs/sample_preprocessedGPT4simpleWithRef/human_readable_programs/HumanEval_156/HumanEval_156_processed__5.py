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
    
    # This postcondition checks if the returned string only contains lowercase roman numerals
    assert all(char in 'mcxidlv' for char in return_value), "The returned string contains non-roman numeral characters"
    

    return return_value
