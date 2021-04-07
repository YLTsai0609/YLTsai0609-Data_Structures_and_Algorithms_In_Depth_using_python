# splay tree - zig zag restructuring

<img src='../assets/216_1.png'></img>

Consider the rotation can reduce the insertion/searched node depth 2 or 1.

The time complexity is $O(d)$, $d$ is the depth of the searched/insertion node.

<img src='../assets/216_2.png'></img>

The time complexity of seaching/insertion/deletion is $O(h)$

There is no grauntee about the height. might be $O(n)$(linked list)