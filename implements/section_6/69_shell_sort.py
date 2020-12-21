'''
Time O(N log N)

Space O(1)

'''


def shell_sort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        i = gap
        # traverse the array
        while i < n:
            temp = A[i]
            j = i - gap  # the left part to compare
            while j >= 0 and A[j] > temp:
                A[j + gap] = A[j]
                j -= gap
            A[j + gap] = temp
            i += 1
        gap = gap // 2


A = [3, 5, 8, 9, 6, 2]


print('original array', A)
shell_sort(A)
print('sorted array', A)
