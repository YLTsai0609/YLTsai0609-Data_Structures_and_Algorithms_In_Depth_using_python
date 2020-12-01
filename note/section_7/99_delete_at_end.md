# Idea

先走到最後面，將tail指到p，tail.next指向None

Edge case : 

    1. 如果一開始就是空的，return
    2. head assign到下一個後，若只剩一個Node，將tail指爲Null

``` Python
Algorithm remove_last()
    if is_empty() then
        print('List is empty')
        return
    p = head
    i = 1 # how many nodes we traveled
    while i < length() - 1
        p = p.next
        i += 1
    tail = p
    p = p.next
    e = element
    tail.next = Null
    size -= 1
```

Time Complexity : $O(N)$

Space Complexity : $O(1)$
