class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class StackLinked:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.is_empty():
            return
        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.is_empty():
            print('Stack is Empty')
            return
        else:
            return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element, end='-->')
            p = p._next
        print()


S = StackLinked()
S.push(5)
S.push(3)
print('Length', len(S))
S.display()
print(S.pop())
print(S.is_empty())
print('Top', S.top())
print(S.pop())
print(S.is_empty())
S.display()
