# shell sort

simliar to selection sort.

<img src='../assets/66_1.png'></img>

1. fill the gap, gap = $\frac{n}{2} = 3$ 
2. compare the right, if bigger, perform swapping
3. compare the left, if bigger, perform swapping
4. gap = gap / 2

# Example

1. get first gap and traverse.

  
<img src='../assets/66_2.png'></img>
<img src='../assets/66_3.png'></img>
<img src='../assets/66_4.png'></img>
<img src='../assets/66_5.png'></img>
<img src='../assets/66_6.png'></img>
<img src='../assets/66_7.png'></img>
<img src='../assets/66_8.png'></img>

2. second gap

gap /= 2 = 3/2 -> we pick 1

<img src='../assets/66_9.png'></img>
<img src='../assets/66_10.png'></img>
<img src='../assets/66_11.png'></img>
<img src='../assets/66_12.png'></img>
<img src='../assets/66_13.png'></img>
<img src='../assets/66_14.png'></img>
<img src='../assets/66_15.png'></img>
<img src='../assets/66_16.png'></img>
<img src='../assets/66_17.png'></img>
<img src='../assets/66_18.png'></img>

3. gap = 0, done.

``` Python
Algorithm shell_sort(A)
  n = length(A)
  for gap = n / 2, gap >0, gap = gap/2
    for i = gap, i < n i++
      gvalue = A[i]
      j = i - gap
      while j >= 0 and A[j] > gvalue
        A[j + gap] = A[j]
        j = j - gap
      A[j + gap] = gvalue
```

# Complexity

Rounds : 

gap = n / 2, gap / 2, gap / 2, ..., 0 -> $O(log N)$

traverse all the array : $O(N)$

Time : $O(N log N)$

Space : O(1)

basically the same with selection sort
