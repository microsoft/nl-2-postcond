def match_parens_original(lst):
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    """

    def valid_parens(s: str) -> bool:
        cnt = 0
        for ch in s:
            cnt = cnt + 1 if ch == '(' else cnt - 1
            if cnt < 0:
                return False
        return cnt == 0
    return 'Yes' if valid_parens(lst[0] + lst[1]) or valid_parens(lst[1] + lst[0]) else 'No'


def match_parens(lst):


    return_value = match_parens_original(lst)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks if the return value is 'Yes', then it is possible to form a balanced parentheses string by concatenating
    # the two strings in any order
    assert (return_value == 'Yes') == (any(all(x >= 0 for x in itertools.accumulate(map({'(': 1, ')': -1}.get, a+b))) for a, b in [lst, lst[::-1]]))
    

    return return_value
