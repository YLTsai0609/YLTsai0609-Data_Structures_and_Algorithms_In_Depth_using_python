'''
'''
from array import array

# 開一個新的array，使用signed integer, 內含 -2, -1, 0, 1, 2
numbers = array('h', [-2, -1, 0, 1, 2])

# 觀察memv物件，長度
memv = memoryview(numbers)
print(memv, len(memv))

# 全部改成unsigned integer，就地更改，不複製新的
memv_oct = memv.cast("B")
print(memv_oct.tolist())

# 把第5個元素改成4
memv_oct[5] = 4

# 可以看到原本的numbers也被更改了，因為是指到同一份記憶體，memoryview幫我們做了記憶體分塊的管理
print(numbers)
