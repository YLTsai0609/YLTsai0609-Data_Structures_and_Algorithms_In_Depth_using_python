'''
digits of maximum element d
array size N

Time O(dN), if N is large, almost O(N)
Space O(1)
'''

# A = [3, 5, 8, 9, 6, 2, 3, 5, 5, 5]
A = [63, 250, 835, 947, 651, 28]

print('original array', A)
A.sort()
# sorted(A)
print('sorted array', A)
