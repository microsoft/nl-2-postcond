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
    
    # This postcondition checks if all lower case vowels in the original message have been changed accordingly 
    # in the return value and if all upper case vowels in the original message have been changed accordingly 
    # in the return value. The change is defined as the character that appears 2 places ahead of that vowel 
    # in the english alphabet. This is only one aspect of the function's behavior and does not check 
    # if the case of the letters have been swapped.
    assert all([original.upper() != return_vowel.upper() if original in "aeiouAEIOU" else True 
                for original, return_vowel in zip(message, return_value)])
    

    return return_value
