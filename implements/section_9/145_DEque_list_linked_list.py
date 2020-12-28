'''
you can inhert linked list
but here we go stand-alone approach for educational purpose
'''


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class DEQueLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_last(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rare._next = newest
        self._rare = newest
        self._size += 1

    def add_first(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
            self._rare = newest
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rare = None
        return e

    def remove_last(self):
        if self.is_empty():
            print('List is empty')
            return
        p = self._front
        i = 1
        while i < len(self) - 1:
            p = p._next
            i += 1
        self._rare = p
        p = p._next
        e = p._element
        self._rare._next = None
        self._size -= 1
        return e

    def display(self):
        p = self._front
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def search(self, key):
        p = self._front
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1

    def first(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._front._element

    def last(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._rare._element


D = DEQueLinked()
D.add_first(5)
D.display()
D.add_first(3)
D.display()
D.add_last(7)
D.display()
D.add_last(12)
D.display()
print('Length : ', len(D))
D.remove_last()
D.display()
D.remove_first()
D.display()
print('the element 7 is at position : ', D.search(7))
print('the first element is : ', D.first())
print('the last element is : ', D.last())
D.display()
