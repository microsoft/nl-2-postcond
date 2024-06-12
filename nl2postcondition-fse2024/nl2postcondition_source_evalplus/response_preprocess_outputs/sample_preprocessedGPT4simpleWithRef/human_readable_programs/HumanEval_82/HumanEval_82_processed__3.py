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
    
    # The postcondition checks if the length of the string is a prime number when the function returns True and not a prime number when the function returns False
    
    assert (return_value and all(len(string) % i for i in range(2, int(len(string)**0.5) + 1))) or (not return_value and any(len(string) % i == 0 for i in range(2, int(len(string)**0.5) + 1)))
    

    return return_value
