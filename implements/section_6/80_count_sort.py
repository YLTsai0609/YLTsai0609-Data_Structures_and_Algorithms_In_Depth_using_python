'''
maximum number M
array size N

Time O(N) or O(M)
Space O(M)

'''


def count_sort(A):
    n = len(A)
    maxsize = max(A)
    carray = [0] * (maxsize + 1)

    # place index to carray
    for i in range(n):
        carray[A[i]] += 1
    i = 0  # index of carray
    j = 0  # index of original array

    # place caaray index to original array
    while i < maxsize + 1:
        if carray[i] > 0:
            A[j] = i
            j += 1
            carray[i] -= 1
        else:
            i += 1


A = [3, 5, 8, 9, 6, 2, 3, 5, 5, 5]


print('original array', A)
count_sort(A)
print('sorted array', A)
