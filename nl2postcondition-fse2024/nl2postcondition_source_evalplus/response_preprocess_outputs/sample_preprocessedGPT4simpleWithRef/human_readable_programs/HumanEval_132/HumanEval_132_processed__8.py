def is_nested_original(string):
    """
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    """
    for i in range(len(string)):
        if string[i] == ']':
            continue
        cnt, max_nest = (0, 0)
        for j in range(i, len(string)):
            if string[j] == '[':
                cnt += 1
            else:
                cnt -= 1
            max_nest = max(max_nest, cnt)
            if cnt == 0:
                if max_nest >= 2:
                    return True
                break
    return False


def is_nested(string):


    return_value = is_nested_original(string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that if the string contains a nested square bracket sequence, the function must return True. 
    # It does so by searching for the pattern of nested brackets '[]' within the string. If it is found, the function should return True.
    assert ('[[]]' in string) == return_value
    

    return return_value
