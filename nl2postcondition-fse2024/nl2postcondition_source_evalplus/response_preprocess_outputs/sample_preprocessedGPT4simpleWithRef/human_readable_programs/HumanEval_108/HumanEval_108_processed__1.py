def count_nums_original(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def judge(x: int) -> int:
        l = list(str(x))
        if l[0] == '-':
            l = l[1:]
            l = list(map(int, l))
            l[0] = -l[0]
        else:
            l = list(map(int, l))
        return 1 if sum(l) > 0 else 0
    return sum(map(judge, arr))


def count_nums(arr):


    return_value = count_nums_original(arr)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return value is not greater than the length of the input list.
    # This is because the function count_nums is counting the number of elements in the list that satisfy a certain condition,
    # so it can't return a count that is greater than the total number of elements in the list.
    assert return_value <= len(arr)
    

    return return_value
