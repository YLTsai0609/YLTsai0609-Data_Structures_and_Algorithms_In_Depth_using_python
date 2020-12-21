# Comparision based sorted algorithms

which compares elements.

| Algorithms | Best Case | Average Case | Worst Case | Space | Stable | Note |
|------------|-----------|--------------|------------|-------|--------|------|
| Selection Sort      | $O(N^2)$     | $O(N^2)$        |     $O(N^2)$       |   $O(1)$    |  No   |  if input array is already sorted, the algorithm will not know that. git $O(N^2)$   |
| Insertion Sort      | $O(N)$     | $O(N^2)$        |     $O(N^2)$       |   $O(1)$    |  Yes   |  the algorithm will not take a lot of time if the array is sorted   |
| Bubble Sort      | $O(N)$     | $O(N^2)$        |     $O(N^2)$       |   $O(1)$    |  Yes   |  the algorithm will not take a lot of time if the array is sorted   |
| Shell Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N^2)$       |   $O(1)$    |  No   |     | 
| Merge Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N log N)$       |   $O(N)$    |  Yes   |  divide and conquer approach   |
| Quick Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N^2)$       |   $O(N)$    |  No   |  divide and conquer approach   |
| Heap Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N log N)$       |   $O(1)$    |  No   |     |

# Indexed based algorithms

| Algorithms | Best Case | Average Case | Worst Case | Space | Stable | Note |
|------------|-----------|--------------|------------|-------|--------|------|
| Count Sort      | $O(N)$     | $O(N)$        |     $O(N)$       |   $O(N)$    |  Yes   |  if the maximum elements is too big, we are using a lot of memory.   |
| Bucket / Bin Sort      | $O(N)$     | $O(N^2)$        |     $O(N^2)$       |   $O(N)$    |  Yes   |   |
| Radix Sort      | $O(N)$     | $O(N)$        |     $O(N)$       |   $O(N)$    |  Yes   |   |
