class QueuesArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        '''
        this dequeue cost 
        Time O(N) due to we use a list interally.
        '''
        if self.is_empty():
            print('Qyeue is Empty')
            return
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        return self._data[0]


Q = QueuesArray()
Q.enqueue(6)
Q.enqueue(3)
print(Q._data)
print('Length : ', len(Q))
Q.enqueue(7)
Q.enqueue(12)
print('Length : ', len(Q))
Q.dequeue()
print('Length : ', len(Q))
Q.first()
print('Length : ', len(Q))
