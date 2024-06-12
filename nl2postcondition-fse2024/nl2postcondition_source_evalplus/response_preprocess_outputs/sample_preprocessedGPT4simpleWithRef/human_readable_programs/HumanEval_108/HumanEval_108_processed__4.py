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
    
    # Postcondition: Checks if the return value is less than or equal to the length of the input array, as the function is counting the number of elements satisfying a certain condition, it cannot return a number greater than the number of elements in the array.
    assert return_value <= len(arr)
    

    return return_value
