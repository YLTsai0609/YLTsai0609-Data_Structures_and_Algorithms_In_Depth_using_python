# Heasp Sort

1. Use Heaps data structure
2. Insert elements in the heap
3. Perform deletion until heap is empty
4. Stor deleted elemenys from the heap back into the array

# Example

<img src='../assets/226_1.png'></img>
<img src='../assets/226_2.png'></img>
<img src='../assets/226_3.png'></img>

perform up heap bubbling

<img src='../assets/226_4.png'></img>

<img src='../assets/226_5.png'></img>
<img src='../assets/226_6.png'></img>

perform up heap bubbling

<img src='../assets/226_7.png'></img>

`deleteMax()` , and down heap bubbling

<img src='../assets/226_8.png'></img>
<img src='../assets/226_9.png'></img>
<img src='../assets/226_10.png'></img>
<img src='../assets/226_11.png'></img>
<img src='../assets/226_12.png'></img>
<img src='../assets/226_13.png'></img>
<img src='../assets/226_14.png'></img>

# Algorithm

``` Python
Algorithm heapsort(A)
   H = heap()
   n = legnth(A)
   for i=0, i < n, i++
     H.insert(A[i])
   
   k = n-1
   for i=0, i < H.current_size, i++
      A[k] = H.deletemax()
      k = k - 1

```

# Complexity

heap.insert -> $O(log n)$, for all items, -> $O(n logn)$

deletion ->  O(logn), for all items, O(n log n) (the n decrease)

Overall, the worst case ->

Time :  $O(n log n)$

Space : $O(n)$
