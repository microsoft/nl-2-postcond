def get_closest_vowel_original(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """

    def is_vowel(ch: str) -> bool:
        return ch in 'aeiouAEIOU'
    for i in range(len(word) - 2, 0, -1):
        if is_vowel(word[i]) and (not is_vowel(word[i - 1])) and (not is_vowel(word[i + 1])):
            return word[i]
    return ''


def get_closest_vowel(word):


    return_value = get_closest_vowel_original(word)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # Checks that the return value is either a vowel or an empty string
    assert (return_value in "aeiouAEIOU" or return_value == ""), "The return value must be a vowel or an empty string"
    

    return return_value
