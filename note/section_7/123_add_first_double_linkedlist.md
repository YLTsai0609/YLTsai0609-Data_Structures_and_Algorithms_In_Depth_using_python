# add first in double linked list

<img src='../asserts/123_1.png'></img>
<img src='../asserts/123_2.png'></img>
<img src='../asserts/123_3.png'></img>

``` Python
Algorithm add_first(e)
    newest = Node(e, Null, Null)
    if is_empty() then
        head = newest
        tail = newest
    else
        newest.next = head
        head.prev = newest # double link
        head = newest
    size += 1
```

Time : $O(1)$

Space : $O(1)$
