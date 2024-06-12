def generate_integers_original(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = (b, a)
    return [i for i in range(a, min(b + 1, 10)) if i % 2 == 0]


def generate_integers(a, b):


    return_value = generate_integers_original(a, b)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: Checks if the return_value contains only even numbers and each number is within the range [a, b] in ascending order
    assert all(i % 2 == 0 and a <= i <= b for i in return_value) and return_value == sorted(return_value)
    

    return return_value