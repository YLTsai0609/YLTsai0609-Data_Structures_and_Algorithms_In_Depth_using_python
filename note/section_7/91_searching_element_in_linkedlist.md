# Idea

只能從頭開始找

``` Python
Algorithm search(key)
    p = head
    index = 0
    while p:
        if p.element == key then
            return index
        p = p.next
        index += 1
    return -1

```

Time Complexity : $O(N)$

Space Complexity : $O(1)$
