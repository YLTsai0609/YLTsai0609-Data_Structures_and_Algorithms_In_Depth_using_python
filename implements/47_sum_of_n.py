def sum_rec(n):
    '''
    1 + 2 + 3 + 4 + ... + n
    recursive way : sum(n) = sum(n - 1) + n
    Time Complexity O(N)
    '''
    if n == 0:
        return 0
    return sum_rec(n - 1) + n


print(sum_rec(4))
