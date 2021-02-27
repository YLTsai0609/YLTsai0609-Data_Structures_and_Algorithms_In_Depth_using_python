'''
python built-in heap module

    starts with index 0 (which is the smallest)
    so the heapq module basically creaes a min heap using a list

'''
import heapq as heap

L1 = []

# Push
heap.heappush(L1, 25)
heap.heappush(L1, 14)
heap.heappush(L1, 2)
heap.heappush(L1, 20)
heap.heappush(L1, 10)

# print(type(heap), dir(heap))
# print(L1)
# Pop
# e = heap.heappop(L1)
# print(e)
# print(L1)

# Push your item first, then pop the root
# e = heap.heappushpop(L1, 35)  # pop root and push 35 into the heap
# you can push 1, and pop, you'll get 1
# print(e)
# print(L1)

# pop and replace the input as root

e = heap.heapreplace(L1, 1)  # pop root and insert 1 as root
# if we insert 100, it will do th bubbling part
print(e)
print(L1)
