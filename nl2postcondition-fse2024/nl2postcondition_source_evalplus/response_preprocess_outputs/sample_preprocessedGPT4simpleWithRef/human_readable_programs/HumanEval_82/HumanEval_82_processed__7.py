def prime_length_original(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    def is_prime(a):
        return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))
    return is_prime(len(string))


def prime_length(string):


    return_value = prime_length_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Postcondition: The return value should be a boolean indicating whether the length of input string is a prime number or not.
    assert isinstance(return_value, bool) and ((len(string) > 1 and all(len(string) % x != 0 for x in range(2, int(len(string) ** 0.5) + 1)) == return_value) or (len(string) <= 1 and return_value == False))
    

    return return_value
