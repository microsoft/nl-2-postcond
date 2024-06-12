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
    
    # This postcondition checks that if a return value is present (i.e., a string of length 1),
    # it must be a vowel that is flanked by two consonants in the input word. 
    # If the return value is an empty string, the postcondition checks that there are no vowels 
    # in the input word that are surrounded by two consonants.
    import re
    assert (len(return_value) == 1 and re.search(f"[^aieouAEIOU]{return_value}[^aieouAEIOU]", word)) or \
           (return_value == "" and not any(re.search(f"[^aieouAEIOU]{vowel}[^aieouAEIOU]", word) for vowel in "aeiouAEIOU"))
    

    return return_value
