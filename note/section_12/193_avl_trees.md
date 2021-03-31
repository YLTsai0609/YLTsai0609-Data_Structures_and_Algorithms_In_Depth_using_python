# AVL Trees

Adelson-Velsky and Landis Tree - The most early developed blanced binary search tree.

Height-balance Property - for every node, height of children differ by at most 1.

<img src='../assets/193_1.png'></img>

AVL Trees : Any binary search tree that satisfies height-balance property.

# Example

<img src='../assets/193_2.png'></img>

height of left sub-tree - hl
height of right sub-tree - hr

50 : hl - hr = 2 - 2 = 0
30 : hl - hr = 1 - 1 = 0
10 : hl - hr = 0 - 0 = 0

<img src='../assets/193_3.png'></img>

Another example 

60 : hl - hr = 2 - 0 = 2
50 : hl - hr = 1 - 0 = 1
30 : hl - hr = 0 - 0 = 0

<img src='../assets/193_4.png'></img>

<img src='../assets/193_5.png'></img>

we defined the AVL trees : the balance factor for all node must in (-1, 0, 1)

# More Examples

<img src='../assets/193_6.png'></img>

<img src='../assets/193_7.png'></img>

Actually the insertion / deletion of AVL trees is similar to binary search.

But we need to reshape the tree every insertion / deletion to make all the nodes well balanced.

The operation of reshaping as known as rotation.
