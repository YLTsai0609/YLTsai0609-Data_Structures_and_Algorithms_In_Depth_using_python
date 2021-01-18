# Python Hash Table

Hash table present a fast searching data structure.
Python Dictionary is a higher level implementation of hash table.

The most naive way is a two dimensional list. So that we can combine a hash function and list data structure to achieve better searching ability.

## Hash Table Getting Start

check [implementation/hash_table_1.py](../implements/hash_table_1.py)

1. use a hash function to assign any element to a indexed bucket.
2. append value into the bucket
3. Done

Worst Case : All the element in the same bucket 
   - Time Complexity :  $O(N)$
   - Space Complexity : $O(N)$

However, if the number of bucket >> the number of elements you insert, You will get average time complexity $O(1)$. Which means you need a **samrt growth size of hash table method in your implementation**

# Reference

[Hash Table implementation in Python [Data Structures & Algorithms]](http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/)

[Problem Solving with Algorithms and Data Structures using Python - 6.5. Hashing](https://runestone.academy/runestone/books/published/pythonds3/SortSearch/Hashing.html#implementing-the-map-abstract-data-type)
