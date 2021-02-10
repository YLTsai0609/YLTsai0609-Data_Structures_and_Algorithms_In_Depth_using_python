# Heap Insertion Algorithm

<img src='../assets/220_1.png'></img>

we'll consider using array-based data structure to represent a binary tree.

the index 0 : we won't put anything here.

<img src='../assets/220_2.png'></img>

csize : current size

hi : heap index

<img src='../assets/220_3.png'></img>

is it match relational property?

<img src='../assets/220_4.png'></img>

``` Python
e > data[ floor[hi / 2] ]
# current value > its parent?
```

under array representation, the parent always be the floor(children / 2)

<img src='../assets/220_5.png'></img>

<img src='../assets/220_6.png'></img>

TBD
