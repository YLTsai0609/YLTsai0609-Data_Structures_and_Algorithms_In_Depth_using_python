'''
Dummy Python Hash Table

Problems : 

1. 不會自動變大的hash table，元素多就被塞爆了
2. 沒有對紀錄Key，只得可以插入同樣的Key，例如同時插入兩個5
'''

from typing import Any, Tuple


class HashTable:
    def __init__(self, size: int = 10):
        self.data = [[] for _ in range(size)]

    def _hash_func(self, e: Any) -> int:
        return hash(e) % len(self.data)

    def __str__(self):
        return f'{self.data}'

    def _growth_bigger(self) -> None:
        pass

    def add(self, e: Any) -> None:
        hash_key = self._hash_func(e)
        self.data[hash_key].append(e)

    def delete(self, e: Any, verbose: bool = False) -> None:
        if not self.exist(e):
            if verbose:
                print('[NotFound] No element found, do nothing')
        else:
            hash_key = self._hash_func(e)
            self.data[hash_key].remove(e)

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
    h.add(5)
    print(f'hash table {h}, is 5 exist?', h.exist(5))
    h.add('dcard')
    print(f'hash table {h}, is dcard exist?', h.exist('dcard'))
    h.delete(5)
    print(f'hash table {h}, is 5 exist?', h.exist(5))
    return True


if __name__ == "__main__":
    test_HashTable_add_exist_delete()
