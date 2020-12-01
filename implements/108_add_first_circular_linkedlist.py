'''
add first on circular linked list
Time O(1)
Spcae O(1)
'''


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class CircularLinkedList:
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
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            newest._next = newest  # circular link
            self._tail = newest
        else:
            self._tail._next = newest  # circluar link
            newest._next = self._head
        self._head = newest
        self._size += 1

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end='-->')
            p = p._next
            i += 1
        print()


c = CircularLinkedList()
c.add_last(7)
c.add_last(3)
c.add_last(12)
c.display()
print('Size : ', len(c))
c.add_first(100)
c.display()
c.add_first(80)
c.display()
print('Size : ', len(c))
