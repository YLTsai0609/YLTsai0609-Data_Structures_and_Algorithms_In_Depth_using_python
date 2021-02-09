# Asymptotic Analysis

漸進式分析

| notation        | means | hint |
|--------------|-------|-------|
|  $\Omega$   |    best case   |    Lower Bound   |
| $O$   |    worst case   |    Upper Bound   |
| $\theta$ |     average case  |       |

In computer science, we always consider the worst case (to make sure our computer compelete the task!)

# Example

linear search a element in `[84, 21, 47, 96, 15]`

Time Complexity

| notation    |
|-------------|
| $\Omega(1)$ |
| $O(n)$      |
|$\theta(n)$|

average case is $\frac{n}{2}$ which is still $n$ by order of growth

# Realworld

業界使用的 big$O$並非學術界的 big $O$，業界所說的big $O$其實意義上比較接近學術界的$\Theta$，因為這個bound比較緊，較具有實際參考價值

https://lucrelin.blogspot.com/2019/04/big-o.html

因此當我們在討論

Worst, Best, Average, 都應該寫$O$
