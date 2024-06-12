def find_max_original(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    mx_ch_cnt, ans = (0, '')
    for word in words:
        ch_cnt = len(set(word))
        if ch_cnt > mx_ch_cnt or (ch_cnt == mx_ch_cnt and word < ans):
            mx_ch_cnt, ans = (ch_cnt, word)
    return ans


def find_max(words):


    return_value = find_max_original(words)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the return value is the string with the maximum number of unique characters among the input words list.
    # If there are multiple strings with maximum unique characters, it checks if the return value is the lexicographically smallest among them.
    assert return_value == min([word for word in words if len(set(word)) == max(map(lambda x: len(set(x)), words))])
    

    return return_value
