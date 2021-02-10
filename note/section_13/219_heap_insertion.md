# Heap Insertion

<img src='../assets/219_1.png'></img>

need to satisfied two property.

1. we should insert new node by following complete binary tree insetion.
2. new node might break the relational property, we need change the node to make them fit the relational property again.(a.k.a. up-heap bubbling)

# Example

<img src='../assets/219_2.png'></img>

<img src='../assets/219_3.png'></img>

<img src='../assets/219_4.png'></img>

<img src='../assets/219_5.png'></img>

violate relational property, perform up-heap bubbling.

<img src='../assets/219_6.png'></img>

<img src='../assets/219_7.png'></img>

<img src='../assets/219_8.png'></img>

violate relational property, perform up-heap bubbling.

<img src='../assets/219_9.png'></img>

still, violate relational property, perform up-heap bubbling.

<img src='../assets/219_10.png'></img>

# Complexity analysis

Insertion : $O(1)$

Up-heap bubbling : $O(h)$, where $h$ is the level of the tree.

also, heap is a complete binary tree structure. so we have $h \propto log(n)$, where $n$ is the number of nodes
