def fun4(i):
    sums = 1
    for j in range(1, i + 1):
        sums *= j
    return sums


n = 100
while n < 1000:
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if n == (fun4(a) + fun4(b) + fun4(c)):
        print(n)
    n += 1
