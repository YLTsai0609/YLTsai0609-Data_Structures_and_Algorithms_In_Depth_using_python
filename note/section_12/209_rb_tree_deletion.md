# Red-Black Trees insertion

Deleting node is same as binary search tree.

6 scenarios (still a lot of dirty work...)


<img src='../assets/209_1.png'></img>

# S1

<img src='../assets/209_2.png'></img>

it's fine. it'll not breaking any rb tree rules.

# S2

<img src='../assets/209_3.png'></img>

delete 70

break rules -> do restructing(rotation)

# S3

<img src='../assets/209_4.png'></img>

# S4

<img src='../assets/209_5.png'></img>

delete 90

85 rotate to position 90

# S5

<img src='../assets/209_6.png'></img>

delete node 80

<img src='../assets/209_7.png'></img>

rotate 70 to 80

# S6

<img src='../assets/209_8.png'></img>

delete 25

node 15 take the place

<img src='../assets/209_9.png'></img>

recoloring

<img src='../assets/209_10.png'></img>

# Summary

1. remove a red node is easy.
2. reomve a black node whatever a leaf node or non-leaf node, it can be complex.(restructing and bst deletion)


