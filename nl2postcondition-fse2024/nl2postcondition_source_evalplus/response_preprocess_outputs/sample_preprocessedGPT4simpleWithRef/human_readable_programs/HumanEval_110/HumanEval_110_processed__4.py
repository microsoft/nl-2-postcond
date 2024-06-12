def exchange_original(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    cnt_odd = len(list(filter(lambda x: x % 2 == 1, lst1)))
    cnt_even = len(list(filter(lambda x: x % 2 == 0, lst2)))
    return 'YES' if cnt_odd <= cnt_even else 'NO'


def exchange(lst1, lst2):


    return_value = exchange_original(lst1, lst2)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that when the function's return value is "YES", there are no odd numbers in lst1 after hypothetical exchanges with lst2
    assert (return_value == "YES") == (all(x % 2 == 0 for x in lst1))
    

    return return_value