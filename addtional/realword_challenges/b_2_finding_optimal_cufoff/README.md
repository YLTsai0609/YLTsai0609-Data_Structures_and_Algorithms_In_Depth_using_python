# 題目

給定一個資料集$D$，有一組資料$x_i$，每組資料有一個模型預測值以及實際值舉例如下

$x_1 : (0.78, 1)$

$x_2 : (0.99, 1)$

$x_3 : (0.66, 1)$

$x_4 : (0.12, 0)$

$x_5 : (0.22, 0)$

$x_6 : (0.34, 0)$

請寫下一個演算法來找出最佳機率切分點以達到最大準確率

應用場景 : AutoML, Auto finding acctording to accuracy, recall, precision, f1-score.

# 題目分析

切分點切下去之後會產生tp, fp, tn, fn，可以透過拆解指標成這4個factor做思考

| pred     | actual | positive | negtive |
|----------|--------|----------|---------|
| positive |      | tp       |    fp     |
| negtive  |      | fn       |    tn     |

Acc = $\frac{tp + tn}{N}$

$N$為總資料筆數，其中tp和tn會隨著切分點不同而變化

1. 先將資料按照model prediction升序排列

$x_4 : (0.12, 0)$

$x_5 : (0.22, 0)$

$x_6 : (0.34, 0)$

$x_3 : (0.66, 1)$

$x_1 : (0.78, 1)$

$x_2 : (0.99, 1)$

2. 每一個資料點做一次切分，並計算Acc，分析如下

| cutoff | pred <br> ground truth | tp    | tn  | acc |     |     |
|--------|-------------------------|-------|-----|-----|-----|-----|
| $1^{st}$ | 0 1 1 1 1 1 <br> 0 0 0 1 1 1      | 3 | 1  |   4/6  |     
| $2^{nd}$ | 0 0 1 1 1 1 <br> 0 0 0 1 1 1      | 3 | 2  |   5/6  |     
| $3^{rd}$ | 0 0 0 1 1 1 <br> 0 0 0 1 1 1      | 3 | 3  |   6/6  |     
| $4^{th}$ | 0 0 0 0 1 1 <br> 0 0 0 1 1 1      | 2 | 3  |   5/6  |     
| $5^{th}$ | 0 0 0 0 0 1 <br> 0 0 0 1 1 1      | 1 | 3  |   4/6  |     
| $6^{th}$ | 0 0 0 0 0 0 <br> 0 0 0 1 1 1      | 0 | 3  |   3/6  |     

3. 根據accuracy找出最大值

Best cufoff : $3^{rd}$

# 有哪些可能的情況與Edge case?

考慮另一種模型預測

該模型預測能力較差，預測positive機率很低，但ground-truth是 1 ($x_5$)

$x_4 : (0.12, 0)$

$x_5 : (0.22, 1)$

$x_6 : (0.34, 0)$

$x_3 : (0.66, 0)$

$x_1 : (0.78, 1)$

$x_2 : (0.99, 1)$

| cutoff | pred <br> ground truth | tp    | tn  | acc |     |     |
|--------|-------------------------|-------|-----|-----|-----|-----|
| $1^{st}$ | 0 1 1 1 1 1 <br> 0 1 0 0 1 1      | 3 | 1  |   4/6  |     
| $2^{nd}$ | 0 0 1 1 1 1 <br> 0 1 0 0 1 1      | 2 | 1  |   3/6  |     
| $3^{rd}$ | 0 0 0 1 1 1 <br> 0 1 0 0 1 1      | 2 | 2  |   4/6 |     
| $4^{th}$ | 0 0 0 0 1 1 <br> 0 1 0 0 1 1      | 2 | 3  |   5/6  |     
| $5^{th}$ | 0 0 0 0 0 1 <br> 0 1 0 0 1 1      | 1 | 3  |   4/6  |     
| $6^{th}$ | 0 0 0 0 0 0 <br> 0 1 0 0 1 1      | 0 | 3  |   3/6  |     

同樣適用

考慮第三種模型，容易被資料混淆的情況，例如$x_{3}$

$x_4 : (0.12, 0)$

$x_5 : (0.22, 0)$

$x_6 : (0.34, 0)$

$x_3 : (0.66, 0)$

$x_1 : (0.78, 1)$

$x_2 : (0.99, 1)$

| cutoff | pred vesus ground truth | tp    | tn  | acc |     |     |
|--------|-------------------------|-------|-----|-----|-----|-----|
| $1^{st}$ | 0 1 1 1 1 1 <br> 0 0 0 0 1 1      | 2 | 1  |   3/6  |     
| $2^{nd}$ | 0 0 1 1 1 1 <br> 0 0 0 0 1 1      | 2 | 2  |   4/6  |     
| $3^{rd}$ | 0 0 0 1 1 1 <br> 0 0 0 0 1 1      | 2 | 3  |   5/6 |     
| $4^{th}$ | 0 0 0 0 1 1 <br> 0 0 0 0 1 1      | 2 | 4  |   6/6  |     
| $5^{th}$ | 0 0 0 0 0 1 <br> 0 0 0 0 1 1      | 1 | 4  |   5/6  |     
| $6^{th}$ | 0 0 0 0 0 0 <br> 0 0 0 0 1 1      | 0 | 4  |   4/6  |   

同樣適用

Input : N個tuple，第一個元素為pred，第二個元素為ground truth
Output : 1個tuple : 切分值 probability, best accuracy

# 可能用到的資料結構&算法

1. 排序算法(bubble sort, merge sort, count sort, radix sort)，有時間複雜度
2. (可優化)計算準確度，每計算一次要耗時$O(N)$，若要有k個切分點，則要花$O(kN)$
3. 可以邊計算Moving Accuracy邊存下當前的最大值，空間複雜度$O(1)$

# 時間複雜度, 空間複雜度分析

綜合以上1, 2, 3項

# Reference

[Roc curve and cut off point. Python](https://stackoverflow.com/questions/28719067/roc-curve-and-cut-off-point-python)
