'''
delete last in circular linked list
Time O(N)
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

    def add_any(self, e, position):
        if position <= 0 or position > len(self):
            print('cannot insert outside of size')
            return
        elif position == 1:
            self.add_first(e)
            return
        else:
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
            print('Circular List is Empty')
            return
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._head = None
            self._tail = None
        return e

    def remove_last(self):
        if self.is_empty():
            print('Circular List is Empty')
            return
        p = self._head
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1
        self._tail = p
        p = p._next
        self._tail._next = self._head
        e = p._element
        self._size -= 1
        return e

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
print('Size : ', len(c))
c.display()
c.remove_first()
c.display()
c.remove_last()
c.display()
