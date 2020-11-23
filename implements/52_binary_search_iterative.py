def binary_search(A, key):
    '''
    Time Complexity O(logN)
    Space Complexity O(1)
    but a sorted array
    '''
    l = 0
    r = len(A) - 1
    while l < r:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            r = mid - 1
        elif key > A[mid]:
            l = mid + 1
    return -1


A = [84, 24, 47, 96, 15]
print(binary_search(sorted(A), 15))
