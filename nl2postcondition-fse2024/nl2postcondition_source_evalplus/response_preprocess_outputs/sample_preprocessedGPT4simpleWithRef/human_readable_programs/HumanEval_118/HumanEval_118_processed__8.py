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
    
    # This postcondition checks whether the return value is an empty string if there are no vowels between consonants in the word.
    assert (return_value == "" if not any(map(lambda i: word[i] in "aeiouAEIOU" and word[i-1] not in "aeiouAEIOU" and word[i+1] not in "aeiouAEIOU", range(1, len(word)-1))) else True)
    

    return return_value
