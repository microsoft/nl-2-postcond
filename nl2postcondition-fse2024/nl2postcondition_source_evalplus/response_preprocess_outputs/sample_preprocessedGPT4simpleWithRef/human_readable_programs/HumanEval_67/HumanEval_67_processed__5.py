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
    
    # The postcondition checks that the return value is a non-negative integer which represents the count of mango fruits in the basket.
    # This is ensured by checking that the difference between the total count of fruits and the sum of apples and oranges is equal to the returned value.
    # The use of `re.findall()` function from regular expressions is to extract the numbers (counts of apples and oranges) from the input string.
    
    import re
    apple_orange_counts = map(int, re.findall(r'\d+', s)) 
    assert return_value == n - sum(apple_orange_counts), "The returned value does not match the expected count of mango fruits"
    

    return return_value
