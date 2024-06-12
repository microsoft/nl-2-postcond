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
    
    # The postcondition checks that the function get_row has correctly identified the locations of integer x in the 2-dimensional list lst.
    # It does this by asserting that for each tuple in the returned list, the value at the corresponding index in lst is indeed x.
    assert all(lst[i][j] == x for (i, j) in return_value)
    

    return return_value
