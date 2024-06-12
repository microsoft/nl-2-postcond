def get_row_original(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    res = []
    for i, l in enumerate(lst):
        for j in range(len(l) - 1, -1, -1):
            if l[j] == x:
                res.append((i, j))
    return res


def get_row(lst, x):


    return_value = get_row_original(lst, x)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that all tuples in the return value have the first element (representing row number) in non-descending order, 
    # and for tuples with the same first element (same row), their second elements (representing column number) are in non-ascending order.
    # This validates the sorting requirement mentioned in the function specification.
    assert all(return_value[i][0] < return_value[i+1][0] or
               (return_value[i][0] == return_value[i+1][0] and return_value[i][1] >= return_value[i+1][1]) 
               for i in range(len(return_value) - 1))
    

    return return_value
