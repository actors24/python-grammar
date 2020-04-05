i=int(input('请输入一位数:\n'))
sum=0
while i!=0:
    a=i%10
    sum+=a
    i//=10
print(sum)
