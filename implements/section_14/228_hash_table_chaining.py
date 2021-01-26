'''

'''

from LinkedList import LinkedList


class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            # each element is a linked list
            # if we want to keep it simple, we can use list of list
            self.hashtable[i] = LinkedList()

    def hashcode(self, key):
        return key % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        self.hashtable[i].add_last(element)

    def search(self, key) -> bool:
        '''
        exist or not
        '''
        i = self.hashcode(key)
        return self.hashtable[i].search(key) != -1

    def display(self):
        for i in range(self.hashtable_size):
            print('[', i, ']', end=' ')
            self.hashtable[i].display()
        print()


H = HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.display()
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
print('Is 28 in the hash table ? ', H.search(28))
print('Is 100 in the hash table ? ', H.search(100))
