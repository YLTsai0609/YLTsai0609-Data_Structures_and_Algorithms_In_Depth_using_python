'''
Insertion of binary search tree
using in-order traversing
'''


class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, troot, e):
        # searching
        if troot:
            if e < troot._element:
                troot._left = self.insert(troot._left, e)
            elif e > troot._element:
                troot._right = self.insert(troot._right, e)
        else:
            # Insertion
            n = _Node(e)
            troot = n
        return troot

    def search_iter(self, key):
        troot = self._root
        while troot:
            if key == troot._element:
                return True
            elif key < troot._element:
                troot = troot._left
            elif key > troot._element:
                troot = troot._right
        return False

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=' ')
            self.inorder(troot._right)


B = BinarySearchTree()
B._root = B.insert(B._root, 50)
B.insert(B._root, 30)
B.insert(B._root, 80)
B.insert(B._root, 10)
B.insert(B._root, 40)
B.insert(B._root, 60)
B.inorder(B._root)
print()
print(B.search_iter(60))
print(B.search_iter(999))
