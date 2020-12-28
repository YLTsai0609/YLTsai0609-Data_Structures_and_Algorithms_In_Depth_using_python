class DEQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def addfirst(self, e):
        # python list insert
        # O(N)
        self._data.insert(0, e)

    def addlast(self, e):
        # python list append O(1) in general
        # worse case is O(N)
        self._data.append(e)

    def removefirst(self):
        # python list pop(0)
        # O(N)
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.is_empty():
            print('DEQue is Empty')
            return
        return self._data.pop()

    def first(self):
        if self.is_empty():
            print("DEQue is Empty")
            return
        return self._data[0]

    def last(self):
        if self.is_empty():
            print('DEQue is empty')
            return
        return self._data[-1]


D = DEQueArray()
D.addfirst(5)
D.addfirst(3)
D.addfirst(7)
print(D._data)
D.addlast(9)
print(D._data)
D.removefirst()
print(D._data)
D.removelast()
print(D._data)
print('first : ', D.first())
print('last : ', D.last())
