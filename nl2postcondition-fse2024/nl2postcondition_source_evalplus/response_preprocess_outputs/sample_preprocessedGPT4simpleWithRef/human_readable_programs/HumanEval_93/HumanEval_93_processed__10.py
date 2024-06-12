def encode_original(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    def switch_case(ch):
        if ord('A') <= ord(ch) <= ord('Z'):
            return chr(ord(ch) + 32)
        elif ord('a') <= ord(ch) <= ord('z'):
            return chr(ord(ch) - 32)
        else:
            return ch

    def vowel_change(ch):
        return ch if ch not in 'aeiouAEIOU' else chr(ord(ch) + 2)
    m = ''.join(map(switch_case, message))
    return ''.join(map(vowel_change, m))


def encode(message):


    return_value = encode_original(message)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Check if the length of the input message is the same as the length of the returned value
    assert len(message) == len(return_value), "The length of the input and output should be the same"
    

    return return_value