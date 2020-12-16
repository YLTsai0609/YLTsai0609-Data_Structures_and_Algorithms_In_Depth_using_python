'''
delete first
Time : O(1)
Space : O(1)
'''


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_last(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def add_any(self, e, position):
        '''
        the convension might be misleading here
        if position = 3,
        it will be
        n1 --> n2 --> your value --> n4 --> n5
        '''
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1


L = LinkedList()
L.add_last(7)
L.add_last(4)
L.add_last(12)
L.display()
print('Size : ', len(L))
L.add_last(8)
L.add_last(3)

# case 1
L.display()
L.remove_first()
L.display()

# case 2

L2 = LinkedList()
L2.remove_first()
L2.display()

# case 3

L3 = LinkedList()
L3.add_first(5)
L3.remove_first()
L3.display()
