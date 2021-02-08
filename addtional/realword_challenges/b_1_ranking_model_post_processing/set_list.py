'''
僅使用List，請實作一個Python的Set
確認是否有重複值 _exist 


時間複雜度 O(N)
空間複雜度 O(1)
'''

import typing


class MySet:
    """
    用list實作的set
    """

    def __init__(self):
        self.data = []

    def __str__(self):
        return f'{self.data}'

    def __len__(self):
        return len(self.data)

    def _exist(self, e: typing.Any) -> None:
        """
        確認資料是否有重複
        時間複雜度 O(N)
        空間複雜度 O(1)
        """
        return e in self.data

    def add(self, e: typing.Any) -> None:
        """
        加入元素到Set
        Args:
            e (typing.Any): 任意元素
        """
        if self._exist(e):
            return
        else:
            self.data.append(e)

    def read(self, e: typing.Any) -> int:
        """
        讀取Set中的元素，若存在則返回Index，不存在則會引發IndexError

        Args:
            e (typing.Any): 任意元素

        Returns:
            int: 該元素index
        """
        return self.data.index(e)

    def delete(self, e: typing.Any) -> bool:
        """
        刪除元素e，
            若存在，則刪除，並return True
            若不存在，則不做動作，return False
        Args:
            e ([Any]): 任意元素
        Returns:
            bool: 該元素是否被刪除
        """
        if self._exist(e):
            self.data.remove(e)
            return True
        else:
            return False


def test_MySet_hash_table_add_read():
    s = MySet()
    s.add(1)
    asset s.read(1) == 0


def test_MySet_hash_table_add_duplicated():
    s = MySet()
    s.add(1)
    s.add(1)
    asset s.read(1) == 0
    asset len(s) == 1


def test_MySet_hash_table_add_delete():
    s = MySet()
    s.add('dcard')
    s.delete('dcard')
    asset len(s) == 0


if __name__ == "__main__":
    test_MySet_hash_table_add_read()
    test_MySet_hash_table_add_duplicated()
    test_MySet_hash_table_add_delete()
    print('PASSED!')
