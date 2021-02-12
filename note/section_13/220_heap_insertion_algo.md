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

<img src='../assets/220_7.png'></img>

<img src='../assets/220_8.png'></img>

<img src='../assets/220_9.png'></img>

<img src='../assets/220_10.png'></img>

we check $e=15$ > data[heap_index] or not

we need to perform up-heap-bobbling

<img src='../assets/220_11.png'></img>

<img src='../assets/220_12.png'></img>

Appreantly, the up-heap bubbling can be design as a recusion function or loop-style function.

``` Python
function heap_insertion(e)
  if curr_size == maxsize then
    print('No Space)
    return
  curr_size += 1
  heap_index = curr_size
  parent_index = floor(heap_index / 2)
  while heap_index > 1 and e > data[parent_index] then
    data[heap_index] = data[parent_index]
    heap_index = parent_index
  data[heap_index] = e
```
