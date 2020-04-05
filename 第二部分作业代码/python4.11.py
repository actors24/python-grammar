i=int(input('请输入一个整数:\n'))
for a in range(1,i+1):
    print(' '*(i-a),'*'*(a*2-1),' '*(i-a))
