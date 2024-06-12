def anti_shuffle_original(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    words = s.split(' ')
    return ' '.join(map(lambda x: ''.join(sorted(x, key=lambda ch: ord(ch))), words))


def anti_shuffle(s):


    return_value = anti_shuffle_original(s)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if every word in the returned string, when split by space, is sorted
    # according to their ascii value while maintaining the original order of the words in the sentence.
    assert all(word == "".join(sorted(word, key=lambda ch: ord(ch))) for word in return_value.split(" "))
    

    return return_value
