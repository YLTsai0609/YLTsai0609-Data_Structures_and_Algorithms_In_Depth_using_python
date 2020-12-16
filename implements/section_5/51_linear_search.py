def linear_search(A, key):
    '''
    Time Complexity O(N)
    Space Complexity O(1)
    '''
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1
    return -1


A = [84, 24, 47, 96, 15]
print(linear_search(A, 15))
