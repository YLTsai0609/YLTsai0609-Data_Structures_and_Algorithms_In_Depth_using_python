'''
Dummy Python Hash Table
'''

import typing


class HashTable:
    def __init__(self, size: int = 10):
        self.data = [[] for _ in range(size)]

    def _hash_func(self, e: typing.Any):
        return hash(e) % len(self.data)

    def __str__(self):
        return f'{self.data}'

    def _growth_bigger(self):
        pass

    def add(self, e: typing.Any) -> None:
        hash_key = self._hash_func(e)
        self.data[hash_key].append(e)

    def delete(self, e: typing.Any) -> None:
        if not self.exist(e):
            print('[NotFound] No element found, do nothing')
        else:
            hash_key = self._hash_func(e)
            self.data[hash_key].remove(e)

    def exist(self, e: typing.Any) -> bool:
        hash_key = self._hash_func(e)
        for bucket_i, existed_element in enumerate(self.data[hash_key]):
            if e == existed_element:
                print(f'[Found] at bucket {hash_key} position {bucket_i}')
                return True
        print('[NotFound]')
        return False


def test_HashTable_add_exist_delete() -> bool:
    h = HashTable()
    print(f'hash table {h}, is 1 exist?', h.exist(1))
    h.add(5)
    print(f'hash table {h}, is 5 exist?', h.exist(5))
    h.add('dcard')
    print(f'hash table {h}, is dcard exist?', h.exist('dcard'))
    h.delete(5)
    print(f'hash table {h}, is 5 exist?', h.exist('5'))
    return True


if __name__ == "__main__":
    test_HashTable_add_exist_delete()
