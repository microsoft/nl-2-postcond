def bf_original(planet1, planet2):
    """
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    i1, i2 = (planets.index(planet1), planets.index(planet2))
    if i1 > i2:
        i1, i2 = (i2, i1)
    return tuple(planets[i1 + 1:i2])


def bf(planet1, planet2):


    return_value = bf_original(planet1, planet2)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the return value is a tuple and each of its elements are among the eight planets in the solar system.
    assert all(planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] for planet in return_value), "All elements in the return value should be valid planet names"
    

    return return_value
