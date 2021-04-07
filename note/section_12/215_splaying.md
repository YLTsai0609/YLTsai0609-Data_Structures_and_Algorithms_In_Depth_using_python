# splay tree - zig zag restructuring

<img src='../assets/215_1.png'></img>

# Example

<img src='../assets/215_2.png'></img>

consider we've inseted/searched node 14.

first we need to perform zig-zag rotation.

<img src='../assets/215_3.png'></img>

<img src='../assets/215_4.png'></img>

Then we need to perform zig-zig rotation.

<img src='../assets/215_5.png'></img>

Then we need to perform zig-zig rotation again

<img src='../assets/215_6.png'></img>

after we put the 14 to the root.

<img src='../assets/215_7.png'></img>

# Summary

splaying is a sequence operation to make sure the insertion/searched node can be moved to the root.