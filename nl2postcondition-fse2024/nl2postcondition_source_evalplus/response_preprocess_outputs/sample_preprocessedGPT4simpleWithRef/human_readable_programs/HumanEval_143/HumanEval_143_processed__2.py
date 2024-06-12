def words_in_sentence_original(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

    def is_prime(a):
        return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))
    return ' '.join(list(filter(lambda word: is_prime(len(word)), sentence.split(' '))))


def words_in_sentence(sentence):


    return_value = words_in_sentence_original(sentence)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that all words in the returned string have prime length
    assert all(is_prime(len(word)) for word in return_value.split(" "))
    

    return return_value
