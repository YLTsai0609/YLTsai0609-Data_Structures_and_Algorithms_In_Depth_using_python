'''
heap sort

Time Complexity : O(n log n)

Space Compleixty : O(n)
'''


class Heap:
    def __init__(self):
        self._maxsize = 10
        self._data = [-1] * self._maxsize
        self._curr_size = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def insert(self, e):
        if self._curr_size == self._maxsize:
            print('No Space in Heap')
            return
        self._curr_size += 1
        heap_idx = self._curr_size
        # up-heap-bubbling
        # heap is not the root node and heap is greater than the parent
        while heap_idx > 1 and e > self._data[heap_idx // 2]:
            # place heap to parent (which is smaller)
            self._data[heap_idx] = self._data[heap_idx // 2]
            # make heap_idx to parent so that we can compare with the parent of parent
            heap_idx = heap_idx // 2
        # the heap_idx is maximum, we throw max element into the index
        self._data[heap_idx] = e

    def max(self):
        if self._curr_size == 0:
            print('Heap is Empty')
            return
        return self._data[1]

    def deletemax(self):
        if self._curr_size == 0:
            print('Heap is empty')
            return
        # delete the root node and swap the last element into the root
        e = self._data[1]
        self._data[1] = self._data[self._curr_size]
        self._data[self._curr_size] = -1  # means no element there(?)
        self._curr_size -= 1

        # i holds parent node, j holds child node
        i = 1
        j = i * 2
        while j <= self._curr_size:
            # compare the child node and neighbor first, pick the greater
            if self._data[j] < self._data[j + 1]:
                j += 1
            # compare the parent node and the child node, pick the greater to parent
            # which is down heap bubbling
            if self._data[i] < self._data[j]:
                temp = self._data[i]
                self._data[i] = self._data[j]
                self._data[j] = temp
                i = j
                j *= 2
            else:
                break
        return e


def heapsort(A):
    H = Heap()
    n = len(A)
    for i in range(n):
        H.insert(A[i])
    k = n - 1  # the index for the array
    for i in range(H._curr_size):
        A[k] = H.deletemax()
        k -= 1


A = [63, 250, 835, 947, 651, 28]

print('Original Array : ', A)
heapsort(A)
print('Sorted Array : ', A)
