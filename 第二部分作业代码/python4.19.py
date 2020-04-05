i=int(input('请输入一个整数:\n'))
count=0
while i!=0:
   i=i&(i-1)
   count+=1
print('二进制下总共有',count,'个1')

