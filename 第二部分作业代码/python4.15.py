i=int(input('请输入一个数:\n'))
for a in range(2,i+1):
    if i%a==0:
        print('这个数不是质数!')
        break
    elif i%a!=0:
        a+=1
        print('这个数是质数!')
        break

