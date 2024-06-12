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
    
    # This postcondition checks if the returned value is a boolean (True if the length of the string is a prime number, False otherwise)
    assert isinstance(return_value, bool)
    

    return return_value
