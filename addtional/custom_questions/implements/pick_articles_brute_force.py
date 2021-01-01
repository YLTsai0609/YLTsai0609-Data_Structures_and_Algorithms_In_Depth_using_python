'''
給定一個文章列表，以及一個排序模型Ranker

文章列表 : [p1, p2, p3, p4, ..., pn]
Ranker : f(pi, pj) -> [>, <, =]

請實作一個演算法，找出前k個分數最優的文章

--------------------------------------


Ranker Model 模擬 : 以比實數大小的方式進行模擬

--------------------------------------

暴力解 : 對文章列表遍歷兩次，並以Counter進行排序

時間複雜度 O(N^2)
空間複雜度 O(N)
'''

from collections import Counter, defaultdict
from typing import Any


class Ranker:
    def pred(self, post_1: Any, post_2: Any) -> str:
        if post_1 > post_2:
            return '>'
        elif post_1 == post_2:
            return '='
        else:
            return '<'


class SelectTopK:
    def __init__(self, k, post_list: list):
        self.k = k
        self.ranker = Ranker()
        self.post_list = post_list

    def solve_brute_force(self) -> list:
        """
        暴力解
        時間複雜度 O(N^2)
        空間複雜度 O(N)
        Returns:
            [list]: 分數最高的前K個文章，會以List[Tuple]的形式回傳
        """
        greater_sign_counter = defaultdict(int)
        # 兩層迴圈 時間複雜度 O(N^2)
        for p in self.post_list:
            for q in self.post_list:
                if p == q:
                    continue
                else:
                    compare_str = self.ranker.pred(p, q)
                    if compare_str == '>':
                        greater_sign_counter[p] += 1
                    elif compare_str == '=':
                        # +0 means do nothing.
                        pass
                    else:
                        greater_sign_counter[p] -= 1
        # Counter排序，時間複雜度O(N log N)
        return Counter(greater_sign_counter).most_common(self.k)


if __name__ == "__main__":
    sol = SelectTopK(k=10, post_list=[i for i in range(10)])
    print(sol.solve_brute_force())
    sol = SelectTopK(k=10, post_list=[i for i in range(100)])
    print(sol.solve_brute_force())
    print("PASSED!")
