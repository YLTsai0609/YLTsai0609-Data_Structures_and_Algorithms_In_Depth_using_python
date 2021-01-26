'''
Hash table with linear probing style with list  
'''


class HashLinearProbe:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size

    def hashcode(self, key):
        return key % self.hashtable_size

    def linear_probe(self, element):
        i = self.hashcode(element)
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != 0:
            j += 1
        return (i + j) % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        if self.hashtable[i] == 0:
            # the bucket is empty
            self.hashtable[i] = element
        else:
            i = self.linear_probe(element)
            self.hashtable[i] = element

    def search(self, key) -> bool:
        '''
        exist or not
        '''
        i = self.hashcode(key)
        j = 0
        while self.hashtable[(i + j) % self.hashtable_size] != key:
            if self.hashtable[(i + j) % self.hashtable_size] == 0:
                return False
            j += 1
        return True

    def display(self):
        print(self.hashtable)


H = HashLinearProbe()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
print('Is 28 in the hash table ? ', H.search(28))
print('Is 100 in the hash table ? ', H.search(100))
