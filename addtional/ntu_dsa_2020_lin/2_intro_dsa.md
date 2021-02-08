# Data Structure and Algorithm 2020 by Hsuan-Tien Lin in NTU 

# Goal of NTU DSA class

1. High Expectation(硬)
2. As good as the best in on the world!

# Class Introduction

<img src='./assets/NtuDsa1_4.png'></img>
<img src='./assets/NtuDsa1_5.png'></img>

* DSA Introduce data structure and algorithm
* Algorithm Design and Analysis focus on design and analysis algorithm and math.

# Motivations of DSA

# What is Algorithm

1. 電腦做事情 -> 程式譜(algorithm)
2. 做菜 -> 食譜
3. 忍者執行暗殺 -> 暗器譜
4. 演奏音樂 -> 樂譜

# Five Criteria of Algorithm

<img src='./assets/NtuDsa1_1.png'></img>

1. input(人給的)
2. output(是否正確)
3. definiteness(可被定義的)
4. finiteness(給電腦算，電腦會停下來)
5. effectivness(電腦可以算得有效)

# Correctness Proof of Algorithm

1. descrete math helps
2. we usually use Mathematical Induction(數學歸納法) to prove the program recusively

   * Actually, Mathematical Induction plays a recursion proof in math! 

<img src='./assets/NtuDsa1_2.png'></img>

# Efficiency of Algorithm

<img src='./assets/NtuDsa1_3.png'></img>

Tree is a highly parallelable structure, we can run it very fast if we want =)

# Pseudo Code

1. like a idea container
2. spoken language of programming
3. concise but understandable for programmer

# Bad Pseudo Code

1. too detailed

``` Python
a = arr[i]
b = arr[minpos]
if a < b then ...
```

why two temp variable???

2. too mysterious

``` Python
minpos, i
a = 0
for b = 1 to len-1
  if arr[b] < arr[a] then ...
```

what is b and a exactly? In general programmer use i, j, k for index in loop

3. too abstract

``` Python
Run a loop that updates minpos in every iterations
```

# Good Pseudo Code

``` Python
sel Sort
  (integer array arr, integer len)
  for i <- 0 to len -1 do
    # find minIndex from arr[i .. len-1]
    min <- getMinIndex(arr[i .. len-1])
    # put arr[min] at arr[i]
    swap(arr[min, arr[i]])
```

# Rule of thumb

Usually better algorithm/data structure

| movement for computer     | designing idea  | note                                                                                   |
|---------------------------|-----------------|----------------------------------------------------------------------------------------|
| `get/insert` | nearby          |                                                                                        |
| `construct/update/remove` | hide the effort | 1. minimum the construction effort <br> 2. minimum the disorder when updating <br> ... |

# Why DSA?

Usually we have to consider two resource of computer : storage, computation

we want to use the resource **properly** -> good program

## Tradeoff of Different Factors

time, space, power, bandwidth, manpower

The factors usually dependent to each other, so we need to design a proper usage.

1. space <--> bandwidth : if you are design a network-related program

2. time <--> manpower : you write a simple program, but it will take a lot of time to make computer work out our result.

   * In some scenario, it's worthy!
   * In the other, it's not. (for critical program make company rich)

3.  time <--> space : list <--> hash-table

## Different Treadeoff on Different Platforms

1. parallel algorithm degining time/manpower
2. distributed system - transmission/computation
3. embedding system - manpower/power

# Moving from coding to designing

Programming != Coding

1. Programming : building house
2. Coding : construction work

Contents when you get a coding job

| step | stage               | note                    |
|------|---------------------|-------------------------|
| 1    | requirement         |                         |
| 2    | analysis            |                         |
| 3    | design              |                         |
| 4    | refinement & coding |                         |
| 5    | verfication         | proof/test/debug/slides |

# Programming Lesson vs DSA

for example, in C programming lessons

| stage  | C      | DSA    |
|--------|--------|--------|
| req    | simple | simple |
| analysis    | simple | simple |
| design | simple | more   |
| coding | ***    | ***    |
| proof  | none   | some   |
| test   | simple | **     |
| debug  | ***    | **     |

# Refernece

[Video](https://www.youtube.com/watch?v=8IOv2fnc01E&list=PLXVfgk9fNX2Kda9rttSvGROCtRQ3Sb8bA&index=2)

[Course Information](https://www.csie.ntu.edu.tw/~htlin/course/dsa20spring/)
