def count_up_to_original(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    ans = []
    isprime = [True] * (n + 1)
    for i in range(2, n):
        if isprime[i]:
            ans.append(i)
            for j in range(i + i, n, i):
                isprime[j] = False
    return ans


def count_up_to(n):


    return_value = count_up_to_original(n)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that all elements in the return list are prime numbers
    assert all(all(return_value[i] % return_value[j] != 0 for j in range(i)) for i in range(len(return_value)))
    

    return return_value
