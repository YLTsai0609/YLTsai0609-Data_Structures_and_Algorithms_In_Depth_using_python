'''
digits of maximum element d
array size N

Time O(dN), if N is large, almost O(N)
Space O(N)
'''


def radix_sort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    # we need a 2d list so that we can add element into the same buckets
    l = []
    bins = [l] * 10
    for i in range(digits):
        for j in range(n):
            # the reminder of 10, 100, 1000 oer round
            e = int(A[j] / pow(10, i) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        # the index of original array, used to rearrange at intermidiate phase
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k += 1


A = [3, 5, 8, 9, 6, 2, 3, 5, 5, 5]
A = [63, 250, 835, 947, 651, 28]

print('original array', A)
radix_sort(A)
print('sorted array', A)
