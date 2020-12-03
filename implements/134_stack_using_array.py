class StacksArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        # will take out the element in stack
        if self.is_empty():
            print('Stack is empty')
            return
        return self._data.pop()

    def top(self):
        # will NOT take out the element in stack
        if self.is_empty():
            print('Stack is empty')
            return
        return self._data[-1]


S = StacksArray()
S.push(5)
S.push(3)
print(S._data)
print("Length : ", len(S))
print(S.pop())
print(S.is_empty())
S.push('abc')
print(S._data)
