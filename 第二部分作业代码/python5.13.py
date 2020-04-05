n=int(input('请输入一个整数:\n'))
for i in range(2,n):
    a = [True] * i
    for j in range(2,i):
        if i%j==0:
            a[j-2]=False
    if False not in a:
         print(i,end=' ')
