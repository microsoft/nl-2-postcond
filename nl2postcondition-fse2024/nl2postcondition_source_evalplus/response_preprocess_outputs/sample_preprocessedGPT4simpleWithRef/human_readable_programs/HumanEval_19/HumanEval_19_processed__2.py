from typing import List

def sort_numbers_original(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    if numbers == '':
        return ''
    return ' '.join(sorted(numbers.split(' '), key=lambda n: to_int[n]))


def sort_numbers(numbers: str) -> str:


    return_value = sort_numbers_original(numbers)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Check that the output string's words correspond to numbers in ascending order
    to_int = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    assert all(to_int[a] <= to_int[b] for a, b in zip(return_value.split(" "), return_value.split(" ")[1:])), "The output string's words are not in ascending order"
    

    return return_value