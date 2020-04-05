def fun1(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


def fun2(m, n):
    sums = 0
    for j in range(m, n + 1):
        if fun1(j):
            sums += 1
            print(j, end=' ')
    print()
    print(f'总共有{sums}个闰年')


fun2(1949, 2019)


def fun3(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


def fun4(a, b):
    sums = 0
    for j in range(a, b + 1):
        if fun3(j):
            print(j, end=' ')
            sums += 1
    print()
    print(f'总共有{sums}个质数')


fun4(100, 200)


def fun5(y, m, d):
    if m < 1 or m > 12:
        return False
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 0 < d <= 31:
            return True
        else:
            return False
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 0 < d <= 30:
            return True
        else:
            return False
    elif m == 2:
        if fun1(y):
            if 0 < d <= 29:
                return True
            else:
                return False
        elif fun1(y):
            if 0 < d <= 28:
                return True
            else:
                return False


def fun6(y, m, d):
    if y < 0:
        print('日期不合法')
    else:
        if fun5(y, m, d):
            print('日期合法！')
        elif fun5(y, m, d):
            print('日期不合法！')


fun6(2019, 12, 2)
