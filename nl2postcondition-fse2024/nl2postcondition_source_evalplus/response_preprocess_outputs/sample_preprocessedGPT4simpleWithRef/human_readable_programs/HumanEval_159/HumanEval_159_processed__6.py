def eat_original(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


def eat(number, need, remaining):


    return_value = eat_original(number, need, remaining)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the total number of carrots eaten (first element of return_value) 
    # is equal to the number of carrots already eaten plus the minimum between the number of carrots 
    # that the rabbit needs to eat and the number of remaining carrots. 
    # This captures the behavior of the function where the rabbit eats as many carrots as it needs, 
    # if available, otherwise it eats all the remaining carrots.
    
    assert return_value[0] == number + min(need, remaining), "Postcondition failed!"
    

    return return_value