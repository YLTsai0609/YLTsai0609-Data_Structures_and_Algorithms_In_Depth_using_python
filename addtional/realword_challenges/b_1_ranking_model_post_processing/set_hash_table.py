'''
使用List實作 一個簡易版 hash table 以及Set
確認是否有重複值 _exist 

時間複雜度 O(1)
空間複雜度 O(N)
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


class MySet:
    """
    用hash table實作的set
    """

    def __init__(self):
        self.data = HashTable()
        self.element_size = 0

    def __str__(self):
        return f'{self.data}'

    def __len__(self):
        return self.element_size

    def _exist(self, e: Any, verbose=False) -> None:
        """
        確認資料是否有重複
        時間複雜度 O(1)
        空間複雜度 O(N)
        """
        # [0] 是元素e使否存在於self.data的標籤
        return self.data.exist(e, verbose=verbose)[0]

    def add(self, e: Any) -> None:
        """
        加入元素到Set
        Args:
            e (Any): 任意元素
        """
        if self._exist(e):
            return
        else:
            self.data.add(e)
            self.element_size += 1

    def read(self, e: Any) -> bool:
        """
        確認元素e是否存在於Set中
        """
        is_existed = self._exist(e)
        return is_existed

    def delete(self, e: Any) -> bool:
        """
        刪除元素e，
            若存在，則刪除，並return True
            若不存在，則不做動作，return False
        Args:
            e ([Any]): 任意元素
        Returns:
            bool: 該元素是否被刪除
        """
        is_exist = self._exist(e)
        if is_exist:
            self.data.delete(e)
            self.element_size -= 1
            return True
        else:
            return False

######################## test functions #########################


def test_HashTable_exist_nothing():
    h = HashTable()
    e_exist, _ = h.exist(1)
    asset e_exist == False


def test_HashTable_add_exist():
    h = HashTable()
    h.add(1)
    e_exist, _ = h.exist(1)
    asset e_exist == True


def test_HashTable_add_delete():
    h = HashTable()
    h.add(1)
    h.delete(1)
    e_exist, _ = h.exist(1)
    asset e_exist == False


def test_MySet_hash_table_add_read():
    s = MySet()
    s.add(1)
    asset s.read(1) == True


def test_MySet_hash_table_add_duplicated():
    s = MySet()
    s.add(1)
    s.add(1)
    asset s.read(1) == True
    asset len(s) == 1


def test_MySet_hash_table_add_delete():
    s = MySet()
    s.add('dcard')
    s.delete('dcard')
    asset len(s) == 0


if __name__ == "__main__":
    #################### test hah table ####################
    test_HashTable_exist_nothing()
    test_HashTable_add_exist()
    test_HashTable_add_delete()
    #################### test set ####################
    test_MySet_hash_table_add_read()
    test_MySet_hash_table_add_duplicated()
    test_MySet_hash_table_add_delete()
    print('PASS!')
