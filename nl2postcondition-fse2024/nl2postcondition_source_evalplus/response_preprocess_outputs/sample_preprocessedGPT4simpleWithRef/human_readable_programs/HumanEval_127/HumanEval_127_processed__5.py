def intersection_original(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """

    def is_prime(a):
        return not (a < 2 or any((a % x == 0 for x in range(2, int(a ** 0.5) + 1))))
    if interval1[0] > interval2[0]:
        interval1, interval2 = (interval2, interval1)
    l, r = (interval2[0], min(interval1[1], interval2[1]))
    return 'YES' if is_prime(r - l) else 'NO'


def intersection(interval1, interval2):


    return_value = intersection_original(interval1, interval2)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # The postcondition checks that the return value is a string and that it is either "YES" or "NO"
    assert isinstance(return_value, str) and return_value in ("YES", "NO")
    

    return return_value
