def fun5(m):
    sums = 1
    while 1:
        if m % 2 == 0:
            print('第', sums, '次计算：', m, '//', 2, '=', end='')
            m //= 2
            print(m)
            sums += 1
        elif m % 2 == 1:
            print('第', sums, '次计算：', m, '*', 3, '+1=', end='')
            m = m * 3 + 1
            print(m)
            sums += 1
        if m == 1:
            break


fun5(20)
