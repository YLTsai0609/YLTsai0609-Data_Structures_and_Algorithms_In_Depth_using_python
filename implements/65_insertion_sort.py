'''
Time O(N^{2})

Space O(1)

Stable sort
'''


def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        cvalue = A[i]
        position = i
        while position > 0 and A[position - 1] > cvalue:
            # the condition indicate two value is sorted or not
            # fi not, performing backward swapping
            A[position] = A[position - 1]
            position -= 1
        A[position] = cvalue


A = [3, 5, 8, 9, 6, 2]

insertion_sort(A)

print('original array', A)
insertion_sort(A)
print('sorted array', A)
