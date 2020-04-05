def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(n, ':', a, '->', c)
        hanoi(n - 1, b, a, c)


def fun(n, a, b, c):
    hanoi(n, a, b, c)


fun(10, 'a', 'b', 'c')
