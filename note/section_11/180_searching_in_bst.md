# Searching in Binary Search Tree

if smaller, search the left sub-tree

else, search the right sub-tree

equal, return the value

search to the leaves -> not exist

# Example

<img src='../assets/180_1.png'></img>
<img src='../assets/180_2.png'></img>

Found!

<img src='../assets/180_3.png'></img>
<img src='../assets/180_4.png'></img>

Found!

<img src='../assets/180_5.png'></img>
<img src='../assets/180_6.png'></img>
<img src='../assets/180_7.png'></img>

Not Found!

return False

# Time Complexity

$O(h)$ - where $h$ is the height of the tree.

# Algorithm - Iteraitve Search Function

``` Python
Algorithm seach_iter(key)
    troot = root
    while troot then
        if key == troot.element then
            return True
        elif key <= troot.element then
            troot = troot.left
        elif key > troot.element ten
            troot = troot.right
    return False
```

# Algortihm - Recirsive Search Function

``` Python
Algorithm search_rec(troot, key)
   if troot then
      if key == troot.element then
          return True
      elif key < troot.element then
          return search_rec(troot.left, key)
      elif key > troot.element then
          return search_rec(troot.right, key) 
   else
       return False
```
