def factorial(n):
    '''
    1x 2 x 3 x 4 + ... x n
    however 1! = 0! = 1
    factorial(n) = factorial(n-1) * n
    Time Complexity O(N) 
    '''
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(4))
