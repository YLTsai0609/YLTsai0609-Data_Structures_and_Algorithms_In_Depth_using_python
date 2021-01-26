'''
bucket sort
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


def hash_func(element, array_length, maxelement):
    # return hash(element) % array_length
    return int(array_length * element / (maxelement + 1))


def bucket_sort(A, bucket_size=10):
    n = len(A)
    maxelement = max(A)
    l = []
    buckets = [l] * bucket_size

    for i in range(n):
        hash_key = hash_func(A[i], n, maxelement)
        if len(buckets[hash_key]) == 0:
            buckets[hash_key] = [A[i]]
        else:
            buckets[hash_key].append(A[i])

    for i in range(bucket_size):
        insertion_sort(buckets[i])

    bucket_i = 0
    for i in range(bucket_size):
        for _ in range(len(buckets[i])):
            A[bucket_i] = buckets[i].pop(0)
            bucket_i += 1


A = [63, 250, 835, 947777777, 651, 28, 555, 345]

print('Origin Array : ', A)
bucket_sort(A)
print('Sorted Array', A)
