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
    
    # This postcondition checks that the sum of the number of even and odd digits is equal to the total number of digits in the absolute value of the input number
    import re
    assert len(re.findall(r'\d', str(abs(num)))) == sum(return_value), "The sum of even and odd digits doesn't match total digits"
    

    return return_value
