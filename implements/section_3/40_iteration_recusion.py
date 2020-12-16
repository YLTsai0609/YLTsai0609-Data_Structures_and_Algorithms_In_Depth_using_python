def calculatr_itr(n):
    '''
    Time : O(N)
    '''
    while n > 0:
        k = n ** 2
        print(k)
        n = n - 1


def calculatr_rec(n):
    if n > 0:  # O(1)
        k = n ** 2  # O(1)
        print(k)  # O(1)
        calculatr_rec(n - 1)  # based on the base case, 4 -> 3 -> 2 -> 1 O(N)


calculatr_itr(4)
calculatr_rec(4)
