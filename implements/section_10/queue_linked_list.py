
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class QueuedLinked:
    def __init__(self) -> None:
        self._front = None
        self._rare = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
        else:
            self._rare._next = newest
        self._rare = newest
        self._size += 1

    def dequeue(self):
        '''
        This method take O(1) to take out the element.
        '''
        if self.is_empty():
            print('Queue is Empty')
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.is_empty():
            self._rare = None
        return e

    def first(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        return self._front._element

    def display(self):
        p = self._front
        while p:
            print(p._element, end='<--')
            p = p._next
        print()


Q = QueuedLinked()
Q.enqueue(6)
Q.enqueue(3)
Q.display()
print('Length : ', len(Q))
Q.enqueue(7)
Q.enqueue(12)
print('Length : ', len(Q))
Q.dequeue()
print('Length : ', len(Q))
Q.first()
print('Length : ', len(Q))
Q.display()
