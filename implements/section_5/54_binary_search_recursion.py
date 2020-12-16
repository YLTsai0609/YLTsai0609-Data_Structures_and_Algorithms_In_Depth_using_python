'''
遞迴版本的參數要寫在外面，因為若在函數內進行初始
每次call fundction的一開始都會重算l和r
'''


def binary_search(A, key, l, r):
    '''
    Time Complexity O(logN) -> 2分法，Time Complexity log2 N
    Space Complexity O(1)
    but a sorted array

    '''
    # base case
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
    # recursion
        elif key < A[mid]:
            return binary_search(A, key, l, mid - 1)
        elif key > A[mid]:
            return binary_search(A, key, mid + 1, r)


A = [84, 24, 47, 96, 15]
print(binary_search(sorted(A), 15, l=0, r=len(A)))
