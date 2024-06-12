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
    
    # This postcondition checks if the count of even and odd digits in the number matches with the return value
    import re
    assert return_value == (len(re.findall("[02468]", str(abs(num)))), len(re.findall("[13579]", str(abs(num)))))
    

    return return_value
