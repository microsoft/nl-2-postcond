def is_bored_original(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = map(lambda x: x.strip(), S.replace('?', '.').replace('!', '.').split('.'))
    return len([s for s in sentences if s.startswith('I ')])


def is_bored(S):


    return_value = is_bored_original(S)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is less or equal to the total number of sentences in the input string. 
    # This holds true as a valid sentence starting with 'I' can at most be counted once, hence the number of boredoms can't exceed total number of sentences.
    import re
    assert return_value <= len(re.split(r'[.?!]', S))
    

    return return_value
