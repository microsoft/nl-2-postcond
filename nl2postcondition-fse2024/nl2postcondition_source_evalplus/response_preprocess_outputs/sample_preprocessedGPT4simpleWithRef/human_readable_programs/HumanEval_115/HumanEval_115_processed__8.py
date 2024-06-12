def max_fill_original(grid, capacity):
    import math
    '\n    You are given a rectangular grid of wells. Each row represents a single well,\n    and each 1 in a row represents a single unit of water.\n    Each well has a corresponding bucket that can be used to extract water from it, \n    and all buckets have the same capacity.\n    Your task is to use the buckets to empty the wells.\n    Output the number of times you need to lower the buckets.\n\n    Example 1:\n        Input: \n            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]\n            bucket_capacity : 1\n        Output: 6\n\n    Example 2:\n        Input: \n            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]\n            bucket_capacity : 2\n        Output: 5\n    \n    Example 3:\n        Input: \n            grid : [[0,0,0], [0,0,0]]\n            bucket_capacity : 5\n        Output: 0\n\n    Constraints:\n        * all wells have the same length\n        * 1 <= grid.length <= 10^2\n        * 1 <= grid[:,1].length <= 10^2\n        * grid[i][j] -> 0 | 1\n        * 1 <= capacity <= 10\n    '
    ans = 0
    for l in grid:
        ans += math.ceil(sum(l) / capacity)
    return ans


def max_fill(grid, capacity):


    return_value = max_fill_original(grid, capacity)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks whether the return value is a non-negative integer. 
    # This is because the number of times to lower the buckets cannot be negative and must be an integer.
    assert isinstance(return_value, int) and return_value >= 0
    

    return return_value
