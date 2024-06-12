def fruit_distribution_original(s, n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    words = s.split(' ')
    c1, c2 = (int(words[0]), int(words[3]))
    assert n - c1 - c2 >= 0, 'invalid inputs'
    return n - c1 - c2


def fruit_distribution(s, n):


    return_value = fruit_distribution_original(s, n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is less than or equal to the total number of fruits.
    # This ensures that the function correctly calculates the number of mangoes, which should always be less than or equal to the total number of fruits.
    assert return_value <= n, "Number of mangoes cannot be more than total fruits"
    

    return return_value
