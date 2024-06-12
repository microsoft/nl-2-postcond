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
    
    # The postcondition checks if the function correctly identifies the length of the string as a prime number.
    # If the function returns True, then the length of the string should be a prime number. If it returns False,
    # then the length of the string should not be a prime number. This is validated by checking if any number up to the square root of the string length divides the string length exactly. 
    
    assert return_value == all(len(string) % i for i in range(2, int(len(string) ** 0.5) + 1)) if len(string) > 1 else False
    

    return return_value
