# insertion sort

* select, insert, done =)

<img src='../assets/64_1.png'></img>
<img src='../assets/64_2.png'></img>
<img src='../assets/64_3.png'></img>
<img src='../assets/64_4.png'></img>
<img src='../assets/64_5.png'></img>
<img src='../assets/64_6.png'></img>
<img src='../assets/64_7.png'></img>
<img src='../assets/64_8.png'></img>
<img src='../assets/64_9.png'></img>
<img src='../assets/64_10.png'></img>
<img src='../assets/64_11.png'></img>
<img src='../assets/64_12.png'></img>
<img src='../assets/64_13.png'></img>
<img src='../assets/64_14.png'></img>
<img src='../assets/64_15.png'></img>
<img src='../assets/64_16.png'></img>
<img src='../assets/64_17.png'></img>
<img src='../assets/64_18.png'></img>
<img src='../assets/64_19.png'></img>

``` Python
Algorithm insertion_sort(A)
  n = length(A)
  for i = 1, i < n, i++
    cvalue = A[i] # cvalue means change values (for swapping)
    position = i
    while position > 0 and A[position - 1] > cvalue
      # check the curr value is sorted or not
      # then perform backward swapping
      A[position] = A[position - 1]
      position = position - 1
    A[position] = cvalue
```

# Stable or Unstable?

<img src='../assets/64_20.png'></img>

the same element will be stuck when compare with

It's a **stable** sort =)

# Complexity

Time : $O(N^{2})$

Space : $O(1)$ - only need temp for swapping value

basically the same with selection sort
