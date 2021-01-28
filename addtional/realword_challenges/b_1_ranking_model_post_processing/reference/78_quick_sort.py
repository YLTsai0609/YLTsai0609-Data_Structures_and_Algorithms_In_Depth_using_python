'''
[On average] Time O(N logN)
[Worst Case] Time O(N^2) reduce to single linked list

Space O(1)

'''


def quick_sort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi - 1)
        quick_sort(A, pi + 1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            # not crossed, and A[i] <= pivot, keep traversing
            i += 1
        while i <= j and A[j] > pivot:
            # not crossed, and A[j] <= pivot, keep traversing
            j -= 1
        if i <= j:
            # cross happened
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


A = [3, 5, 8, 9, 6, 2]


print('original array', A)
quick_sort(A, 0, len(A) - 1)
print('sorted array', A)
