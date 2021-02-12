'''
we'll using array-based representation of a complete binary tree
then construct heap data structure
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


S = Heap()
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
print(S._data)
S.insert(40)
print(S._data)
