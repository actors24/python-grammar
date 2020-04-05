def fun8(i):
    sums = 0
    for j in range(2,i):
        if i % j == 0:
            sums += 1
    if sums == 0:
        return i
    else:
        return 0


m=int(input('请输入一个不小于6的偶数：'))
for a in range(3,m//2+1):
    for b in range(m//2,m):
        if fun8(a) + fun8(b) == m:
            print(a,b)
        else:
            continue