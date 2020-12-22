'''
獨二進位檔案比文字檔案快60倍，並且比起python list使用更少記憶體
從 80,000,000 <- 181,515,739 縮小兩倍多
'''
from array import array
from random import random

# 建立Array typecode 'd' doubled 雙精度浮點數，
# 給一個generator，從0 到 10**7
floats = array('d',
               (random() for i in range(10 ** 7))
               )

# 支援indexing
print(floats[-1])

# 存成2進位
fp = open('float.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')

# 從2進位檔案載入
fp = open('float.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()

print(floats2[1])

print(floats2 == floats)
