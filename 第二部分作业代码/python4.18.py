i=int(input('请输入一个整数:\n'))
a=0
b=1
sum=0
print(0,end=',')
while sum<i-1:
    print(b,end=',')
    a,b=b,a+b
    sum+=1

