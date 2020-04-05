def fun(n):
    sums = 0
    while n != 0:
        n //= 10
        sums += 1
    print(f'这个数是{sums}位数')


fun(123456)
