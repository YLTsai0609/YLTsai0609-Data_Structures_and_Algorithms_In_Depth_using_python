# Post processing of ranking model

approach 1 : binary-pick

approach 2 : quick select

# approach 1 : binary-pick

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

# approach quick select

[快速選擇 維基百科](https://zh.m.wikipedia.org/zh-tw/%E5%BF%AB%E9%80%9F%E9%80%89%E6%8B%A9)

same author from quick sort, same idea, a kind of partial sort algoeithm.

TODO

check [this](https://www.itread01.com/content/1545039782.html)
