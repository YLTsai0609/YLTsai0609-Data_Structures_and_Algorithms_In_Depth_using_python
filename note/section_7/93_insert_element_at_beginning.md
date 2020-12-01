# Idea

開一個Node，放第一個，指向原來的(如果原本存在)
這裡採用雙指標(head, tail)

``` Python
Algorithm addfirst(e)
    newest = Node(e, Null)
    if is_empty() then
        head = newest
        tail = newest
    else
        newest.next = head
        head = newest
    size += 1

```

Time Complexity : $O(1)$

Space Complexity : $O(1)$
