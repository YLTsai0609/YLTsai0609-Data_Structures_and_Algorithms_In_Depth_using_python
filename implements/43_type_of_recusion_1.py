def calculate_tail(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate_tail(n - 1)


def calculate_head(n):
    if n > 0:
        calculate_head(n - 1)
        k = n ** 2
        print(k)


calculate_tail(4)
calculate_head(4)
