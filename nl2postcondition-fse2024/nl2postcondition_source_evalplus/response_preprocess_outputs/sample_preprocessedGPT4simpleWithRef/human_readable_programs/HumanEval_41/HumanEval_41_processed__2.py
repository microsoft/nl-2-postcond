def car_race_collision_original(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    return n ** 2


def car_race_collision(n: int):


    return_value = car_race_collision_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks whether the returned value is a perfect square
    assert return_value == int(return_value ** 0.5) ** 2
    

    return return_value
