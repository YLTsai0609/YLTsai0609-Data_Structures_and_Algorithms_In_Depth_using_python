'''
delete any from double linked list
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

    def add_any(self, e, position):
        if position == 0:
            self.add_first(e)
        elif position == len(self):
            self.add_last(e)
        elif position > len(self):
            print('your linked list is too short')
        else:
            newest = _Node(e, None, None)
            p = self._head
            i = 1
            while i < position - 1:
                p = p._next
                i += 1
            newest._next = p._next
            p._next._prev = newest  # double link
            p._next = newest
            newest._prev = p  # double link
            self._size += 1

    def remove_first(self):
        if self.is_empty():
            print('List is Empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

    def remove_last(self):
        if self.is_empty():
            print('List is empty')
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        return e

    def remove_any(self, position):
        if position == 0:
            self.remove_first()
        elif position > len(self):
            print('your link list is too short')
            return
        else:
            p = self._head
            i = 1
            while i < position - 1:
                p = p._next
                i += 1
            e = p._next._element
            p._next = p._next._next
            p._next._prev = p
            self._size -= 1
            return e

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
L.remove_last()
L.display()
ele = L.remove_any(3)
print(ele)
L.display()

ele = L.remove_any(3)
print(ele)
L.display()

ele = L.remove_any(3)
print(ele)
L.display()
