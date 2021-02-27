'''
python built-in heap module

    starts with index 0 (which is the smallest)
    so the heapq module basically creaes a min heap using a list

'''
import heapq as heap

L1 = [20, 14, 2, 15, 10, 21]

print(L1)
heap.heapify(L1)
print(L1)

print(heap.nsmallest(3, L1))
print(heap.nlargest(3, L1))
