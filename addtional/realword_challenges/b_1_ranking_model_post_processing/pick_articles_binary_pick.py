'''
給定一個文章列表，以及一個排序模型Ranker

文章列表 : [p1, p2, p3, p4, ..., pn]
Ranker : f(pi, pj) -> [>, <, =]

請實作一個演算法，找出前k個分數最優的文章

--------------------------------------

Edge Case : 同分數的文章處理方式
    - 採Random選取

Ranker Model 模擬 : 以比實數大小的方式進行模擬

--------------------------------------

Binary pick : 借助Binary Search的思想，
              1. 每次從unrank_post_set中N篇文章中找出相對排序最前面1個
              2. 重複以上流程k次
              3. Divide and Conquer Approach

時間複雜度 O(k log N)
空間複雜度 O(N)

'''

from random import choice
from typing import Any
from boltons.setutils import IndexedSet
import time


class Ranker:
    def pred(self, post_1: Any, post_2: Any) -> str:
        if post_1 > post_2:
            return '>'
        elif post_1 < post_2:
            return '<'
        else:
            return '='

    def compete(self, post_1: Any, post_2: Any) -> Any:
        compete_flag = self.pred(post_1, post_2)
        if compete_flag == '>':
            return post_1
        elif compete_flag == '<':
            return post_2
        else:
            # 同分時預設隨機選一個
            return choice([post_1, post_2])


def binary_pick(ranker: Ranker, unrank_post_set: IndexedSet,
                left: int, right: int) -> Any:
    """
    借助Binary Search的思想，每次從unrank_post_set中N篇文章中找出相對排序最前面1個
    Divide and Conquer Approach
    Args:
        ranker : 排序模型
        unrank_post_set (IndexedSet): 未排名的文章集合
        left (int): left index
        right (int): right index

    Returns:
        int: 最佳排名的文章物件
    """
    if left == right:
        # 集合中僅剩一篇文章
        return unrank_post_set[left]
    elif right - left == 1:
        # 集合中僅剩兩篇文章，可透過Ranker進行相對排序，取得相對排序較好的文章物件
        return ranker.compete(unrank_post_set[left], unrank_post_set[right])
    else:
        mid = (left + right) // 2  # 需要整數以便進行list的indexing
        return ranker.compete(binary_pick(ranker, unrank_post_set, left, mid),
                              binary_pick(ranker, unrank_post_set, mid + 1, right))


class SelectTopK:
    def __init__(self, top_k, post_list: list):
        self.top_k = top_k
        self.ranker = Ranker()
        self.post_list = post_list

    def __str__(self):
        return f'n posts : {len(self.post_list)}, pick top {self.top_k}'

    def solve_binary_pick_k(self, show_spent_time: bool = True) -> list:
        """
        借助Binary Search的思想，每次從post_list中N篇文章中找出相對排序最前面1個，重複k次
        時間複雜度 O(k log N)
        空間複雜度 O(N)
        Returns:
            [list]: Top-K articles
        """
        if show_spent_time:
            start = time.time()
        top_k_posts_list = []
        n_picks = 0
        post_set = IndexedSet(self.post_list)
        # 一個重複k次的迴圈，時間複雜度 O(k)
        while n_picks < self.top_k:
            # binary pick，採Divide and Conquer，時間複雜度 O(log N)
            curr_best_post = binary_pick(
                self.ranker,
                post_set, left=0,
                right=len(post_set) - 1)
            top_k_posts_list.append(curr_best_post)  # 加入元素到list 時間複雜度 O(1)
            # 從IndexableSet移除元素，時間複雜度O(1) (HashTable)
            post_set.remove(curr_best_post)
            n_picks += 1
        if show_spent_time:
            spent = (time.time() - start) * 1000
            print(self)
            print(f'spent time {spent:.2f} ms')
        return top_k_posts_list


def test_binary_pick_small():
    post_set = [i for i in range(10)]
    post_set = IndexedSet(post_set)
    ranker = Ranker()
    asset binary_pick(ranker=ranker, unrank_post_set=post_set,
                      left=0, right=len(post_set) - 1) == 9


def test_binary_pick_big():
    post_set = IndexedSet([i for i in range(10000)])
    ranker = Ranker()
    asset binary_pick(ranker=ranker, unrank_post_set=post_set,
                      left=0, right=len(post_set) - 1) == 9999


if __name__ == "__main__":
    test_binary_pick_small()
    test_binary_pick_big()
    for posts_size in [10, 10 * 2, 10 * 4, 10 * 8,
                       50000, 50000 * 2, 50000 * 4, 50000 * 8]:
        sol = SelectTopK(top_k=10, post_list=[i for i in range(posts_size)])
        print('-' * 60)
        picked_top_k = sol.solve_binary_pick_k()
        print(picked_top_k)
    print('PASSED!')
