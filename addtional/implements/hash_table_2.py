'''
Python Hash Table

1. Add growth ability
2. Search element exist when you wanna add something
'''

from typing import Any, Tuple


class HashTable:
    def __init__(self, bucket_size: int = 10):
        self.data = [[] for _ in range(bucket_size)]
        self.element_size = 0
        self.occupied_bucket = 0

    def _hash_func(self, e: Any) -> int:
        return hash(e) % len(self.data)

    def __str__(self):
        return f'{self.data}, element_size : {self.element_size}, occupied_bucket : {self.occupied_bucket}'

    def __len__(self):
        return self.element_size

    def _growth_bigger(self, growth_factor: float = 0.5) -> None:
        extra_buckets = [[] for _ in range(
            int(len(self.data) * growth_factor)
        )]
        self.data.extend(extra_buckets)
        print(
            f'[Growth hit] there are {len(self.data)} buckets in your hash table ')

    def _are_buckets_overcrowded(self, frac: float = .7):
        return self.occupied_bucket > frac * len(self.data)

    def _prune_smaller(self):
        pass

    def _are_buckets_over_sparsed(self, frac: float = .7):
        pass

    def add(self, e: Any) -> None:
        is_existed, _ = self.exist(e)
        if is_existed:
            return
        else:
            hash_key = self._hash_func(e)
            if len(self.data[hash_key]) == 0:
                # check if we using a new bucket
                self.occupied_bucket += 1
            self.data[hash_key].append(e)
            self.element_size += 1
        if self._are_buckets_overcrowded():
            self._growth_bigger()

    def delete(self, e: Any, verbose: bool = False) -> None:
        if not self.exist(e):
            if verbose:
                print('[NotFound] No element found, do nothing')
        else:
            hash_key = self._hash_func(e)
            self.data[hash_key].remove(e)
            if len(self.data[hash_key]) == 0:
                # check if we reduce a bucket to empty
                self.occupied_bucket -= 1
            self.element_size -= 1

    def exist(self, e: Any,
              verbose: bool = False) -> Tuple[
            bool, Any]:
        """
        確認值是否存在於hash table中，
            若存在，回傳True, 該元素
            若不存在，回傳False, -1

        Args:
            e (Any): 任意元素
            verbose (bool, optional): [是否顯示尋找元素的詳細訊息]. Defaults to False.

        Returns:
            Tuple[bool, Any]: 搜尋結果
        """
        hash_key = self._hash_func(e)
        for bucket_i, existed_element in enumerate(self.data[hash_key]):
            if e == existed_element:
                if verbose:
                    print(f'[Found] at bucket {hash_key} position {bucket_i}')
                return True, e
        if verbose:
            print(
                f'[NotFound] you are searching element : {e}, but {e} does not exist')
        return False, -1


def test_HashTable_add_exist_delete() -> bool:
    h = HashTable()
    print(f'hash table {h}, is 1 exist?', h.exist(1))
    h.add(5)
    print(f'hash table {h}, is 5 exist?', h.exist(5))
    h.add('dcard')
    print(f'hash table {h}, is dcard exist?', h.exist('dcard'))
    h.delete(5)
    print(f'hash table {h}, is 5 exist?', h.exist(5))
    return True


def test_HashTable_growth() -> bool:
    h = HashTable()
    for i in range(50):
        print(i)
        h.add(i)
        # print(h)


if __name__ == "__main__":
    test_HashTable_add_exist_delete()
    test_HashTable_growth()
