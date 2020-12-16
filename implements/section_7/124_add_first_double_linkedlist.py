'''
add first into double linked list
Time O(1)
Spcae O(1)
'''


class _Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element, next, prev):
        self._element = element
        self._next = next
        self._prev = prev


class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_last(self, e):
        newest = _Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def display_rev(self):
        p = self._tail
        while p:
            print(p._element, end='-->')
            p = p._prev
        print()


L = DoubleLinkedList()
L.add_last(7)
L.add_last(4)
L.add_last(12)
L.display()
L.display_rev()
print('Size : ', len(L))
L.add_first(25)
L.display()
L.display_rev()
print('Size : ', len(L))
