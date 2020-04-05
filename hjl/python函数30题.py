def fun7(i):
    sums = 0
    for j in range(1, i):
        if i % j == 0:
            sums += j
    return sums


for a in range(2, 3001):
    b = fun7(fun7(a))
    if a == b and a < fun7(a):
        print(a, fun7(a))
