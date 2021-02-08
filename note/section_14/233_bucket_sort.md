# Bucket sort

Use the concept of hashing.

1. Hashing all elements into buckets

2. insertion sort in each bucket

3. retrieve element into a array.

## Example

<img src='../assets/233_1.png'></img>

floor( index = n * e / (max + 1) )

n (the number of element) = 6

max = 92

### inserting

<img src='../assets/233_2.png'></img>
<img src='../assets/233_3.png'></img>
<img src='../assets/233_4.png'></img>
<img src='../assets/233_5.png'></img>
<img src='../assets/233_6.png'></img>
<img src='../assets/233_7.png'></img>
<img src='../assets/233_8.png'></img>

### insertion sort in each bucket

<img src='../assets/233_9.png'></img>

### retreve element

<img src='../assets/233_10.png'></img>

# Algorithm

``` Python
Algorithm bucketsort(A)
    n = length(A)
    max = maximum(A)
    buckets = []
    for i = 0, i < n, i++
        j = n * A[i] / max + 1 # the hash function
        buckets[j] = A[i] # link them?
    for i = 0, i < 10, i++
        inserttionsort(buckets[i])
    k = 0
    for i = 0, i < 10, i++
        A[k] = bucket[i].remove()
        k = k + 1
```

# Complexity Analysis

1. assign to bucket $O(N)$
2. insertion sort $O(m^{2})$, m is the element counts in the bucket
3. Note that the insertion sort part can be parallelized to each bucket.

Space Complexity : $O(n k)$ 

<img src='../assets/233_12.png'></img>

<img src='../assets/233_13.png'></img>

# Reference

[Rust Algorithm Club](https://rust-algo.club/sorting/bucket_sort/)

[tutorials point](https://www.tutorialspoint.com/Bucket-Sort)
