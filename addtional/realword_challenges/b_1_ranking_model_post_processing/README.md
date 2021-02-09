# Post processing of ranking model

approach 1 : binary-pick

approach 2 : quick select

# *Approach I : binary-pick*

Input : posts : $\{p_1, p_2, ...p_N\}$ 

Output : give top $k$ best post 

by algorithm $A$ and Ranking model $f(p_1, p_2) = \{>, <, =\}$

## psud ocode

``` Python
algortihm binary_pick(list_of_post)
    top = []
    for i in range(k):
        curr_best = binary_search(list_of_post)
        top.append(curr_best)
        list_of_post.remove(curr_best)
    return curr_best
```

Seems failed, each time we call binary search

``` 

supporse 8 posts
                p7
                |
        p4              p7  
        |              |
   p2      p4      p5     p7
   |       |       |      |
p1  p2  p3  p4  p5  p6  p7 p8
```

We use 7 function calls, time complexity : $O(N-1)$

So the time complexity pick top $k$

$O(N-1) + O(N-2) + ... + O(N-k)$ ~ $O(kN)$

Which is not $O(klogN)$ - I cliamed

# *approach II quick select*

[快速選擇 維基百科](https://zh.m.wikipedia.org/zh-tw/%E5%BF%AB%E9%80%9F%E9%80%89%E6%8B%A9)

same author from quick sort, same idea, a kind of partial sort algoeithm.

check [this](https://www.itread01.com/content/1545039782.html)

## psudo code

quick_select(input_list, k):

    1. pivot = random(input_list)
    2. partition_point, smaller, greater = _partition(input_list, pivot)
    3. if len(larger) == 5:

            return larger
    elif len(larger) < 5:
            quick_select(smaller)
    else:
        quick_select(larger)

_partition(input_list, pivot):

    less, equal, greater = [], [], []
    for element in input_list:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)

## complexity analysis

### Average case :

everytime, the greater and less ~ $\frac{N}{2}$

Time spend $T(N)$ calculated by number of function calls

number of iterations : $r$

$$
T(N) = N + \frac{N}{2} + \frac{N}{4} + ... + + \frac{N}{2^{r-1}}
$$

how to calculate $T$ ?

It's a geometric series.

$$
T(N) = N + \frac{N}{2} + \frac{N}{4} + ... +  \frac{N}{2^{r-1}} ~ ...(1)
$$

$$
\frac{T(N)}{2} = \frac{N}{2} + \frac{N}{4} + ... + \frac{N}{2^{r-1}} + \frac{N}{2^{r}}~ ...(2)
$$

$$
(1) - (2) : \frac{T(N)}{2} = N - \frac{N}{2^{r}}
$$

we get : 

$T(N) = 2N - \frac{N}{2^{r}}$ ~ $2N$

And finally, our algorithms stops when $2^{r}=N$

So 

$T(N) = 2N - 1 ~～~ 2N$

The algorithm is not depends on $k$, which is better than *Approach I : binary-pick*.

### Worst case

worst case which is always get one more smaller:

Total function calls :

$$
T(N) = N + N-1 + ... +  N-r-1 + .... ～ N^{2}
$$

### Best case 

best case give us only one shot to get $k$ greater elements

$$
T = N
$$

### Summary

| Case    | $T(N)$        |
|---------|------------|
| Worst   | $O(N^{2})$ |
| Average | $O(2N)$    |
| Best    | $O(N)$     |

where $N$ represents the number of samples.
