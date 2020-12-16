'''
This program implement node, inked list and
how to traversing and display a linked list

about __slot__ : efficients way to get attribute in class
https://stackoverflow.com/questions/472000/usage-of-slots
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

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


L = LinkedList()
L.add_last(7)
L.add_last(4)
L.add_last(12)
L.display()
print('Size : ', len(L))
L.add_last(8)
L.add_last(3)
print('Size : ', len(L))
