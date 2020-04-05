def fac(n):
    if n<3:
        return 1
    else:
        return fac(n-2)+fac(n-1)
for i in range(1,13):
    print(fac(i))