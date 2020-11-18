def calculate_tree(n):
    if n > 0:
        calculate_tree(n - 1)
        k = n ** 2
        print(k)
        calculate_tree(n - 1)


calculate_tree(3)
