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
    
    # The postcondition checks if the sum of the counts of even and odd digits in the number is equal to the length of the number (ignoring any negative sign)
    assert sum(return_value) == len(str(abs(num)))
    

    return return_value
