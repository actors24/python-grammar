def fac():
    m = int(input('请输入一个整数:'))
    for i in range(1, m):
        if m % i == 0:
            print(i, end=' ')


fac()
