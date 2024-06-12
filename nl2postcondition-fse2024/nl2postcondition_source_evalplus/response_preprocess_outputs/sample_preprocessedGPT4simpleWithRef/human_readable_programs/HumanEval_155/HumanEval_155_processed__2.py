def even_odd_count_original(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even, odd = (0, 0)
    for ch in str(num):
        if ch in '02468':
            even += 1
        if ch in '13579':
            odd += 1
    return (even, odd)


def even_odd_count(num):


    return_value = even_odd_count_original(num)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Check if the sum of the count of even and odd digits equals the total count of digits in the number
    import re
    assert sum(return_value) == len(re.sub(r'\D', '', str(num))), "The total count of even and odd digits should be equal to the total count of digits in the number"
    

    return return_value
