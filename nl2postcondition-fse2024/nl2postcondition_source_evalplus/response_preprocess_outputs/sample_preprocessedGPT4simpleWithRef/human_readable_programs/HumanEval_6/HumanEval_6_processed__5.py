from typing import List

def parse_nested_parens_original(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def count_depth(s: str) -> int:
        max_depth, cnt = (0, 0)
        for ch in s:
            if ch == '(':
                cnt += 1
            if ch == ')':
                cnt -= 1
            max_depth = max(max_depth, cnt)
        return max_depth
    return [count_depth(s) for s in paren_string.split(' ') if s != '']


def parse_nested_parens(paren_string: str) -> List[int]:


    return_value = parse_nested_parens_original(paren_string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the length of the list returned by the function is equal to the number of non-empty groups of parentheses in the input string.
    assert len(return_value) == len([group for group in paren_string.split(' ') if group != ''])
    

    return return_value