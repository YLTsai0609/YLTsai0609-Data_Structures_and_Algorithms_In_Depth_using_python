# bubble sort

1. If left element is greater than the right element, swap them.
2. traverse the original array, you will get a maximum element at the last element.

<img src='../assets/68_1.png'></img>
<img src='../assets/68_2.png'></img>
<img src='../assets/68_3.png'></img>
<img src='../assets/68_4.png'></img>
<img src='../assets/68_5.png'></img>
<img src='../assets/68_6.png'></img>
<img src='../assets/68_7.png'></img>
<img src='../assets/68_8.png'></img>
<img src='../assets/68_9.png'></img>

# second round

<img src='../assets/68_10.png'></img>
<img src='../assets/68_11.png'></img>
<img src='../assets/68_12.png'></img>
<img src='../assets/68_13.png'></img>
<img src='../assets/68_14.png'></img>
<img src='../assets/68_15.png'></img>

and third, forth, fifth...

As you could see, the value will sorted partially every iteration, like bubble comes up on the water. It's the name bubble sort.

``` Python
Algorithm bubble_sort(A)
  n = length(A)
  for pass = n-1, pass >=0
    for i = 0, i < pass, i++
      if A[i] > A[i+1] then
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp
```

# Stable or Unstable?

<img src='../assets/68_16.png'></img>
<img src='../assets/68_17.png'></img>

stable!

# Complexity

Time : $O(N^{2})$

Space : $O(1)$
