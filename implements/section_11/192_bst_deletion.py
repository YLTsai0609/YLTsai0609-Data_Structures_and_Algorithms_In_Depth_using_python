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

    def delete(self, e):
        p = self._root  # pointer
        pp = None  # parent of pointer
        # find the element you wanna delet
        while p and p._element != e:
            pp = p  # record the parent
            if e < p._element:
                p = p._left
            else:
                p = p._right
        # Not Found
        if not p:
            return False
        # Found, pick a deletion strategy
        if p._left and p._right:
            s = p._left
            # pick largest element of left subtree
            ps = p
            while s._right:
                ps = s
                s = s._right
            # replace node p with largest element of left subtree
            p._element = s._element
            p = s
            pp = ps
        # have one subtree!
        c = None
        # there is a left subtree
        if p._left:
            c = p._left
        else:
            c = p._right
        # if p is the only-one node
        if p == self._root:
            self._root = None
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp._right = c

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
# print(B.search_iter(60))
# print(B.search_iter(999))
print()
B.delete(60)  # leaf node
B.inorder(B._root)
B.delete(50)  # root node
print()
B.inorder(B._root)
