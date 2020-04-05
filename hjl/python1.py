n=int(input('请输入一个整数'))
sum=0
while n!=0:
    b=n%10
    sum+=b
    n//=10
print('其各位数之和:',sum)
