# Heap Deletion

we cannot remove anything we want, we need to make sure our heap still

1. a complete binary tree.(replace by the last node)
2. follow relational property(we need perform down-heap bubbling)

<img src='../assets/222_1.png'></img>

# Example

<img src='../assets/222_2.png'></img>
<img src='../assets/222_3.png'></img>
<img src='../assets/222_4.png'></img>

You might think why we replace the root as 20, complete?

Maybe it's a harder algorithm to design, we start from simplest.

<img src='../assets/222_5.png'></img>

down heap bubbleing, swap 2 and 20.

<img src='../assets/222_6.png'></img>

# Another Example

Consider `deleteMax()` , 

swap the last element into the root.

<img src='../assets/222_7.png'></img>

down heap bubbling

<img src='../assets/222_8.png'></img>

down heap bubbling
<img src='../assets/222_9.png'></img>

down heap bubbling

<img src='../assets/222_10.png'></img>

# Time Complexity

replace : $O(1)$

down-heap-bubbling : $O(log n)$ - due to the worst case of swapping. might perform $h$ times. where $h$ is the height of the tree.
