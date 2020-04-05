y=int(input('请输入年份:'))
m=int(input('请输入月份'))
d=int(input('请输入天数'))
if y<2000:
    print('输入有误，请重新输入')
elif m>12:
    print('输入有误，请重新输入')
elif (not (y%4==0 and y%100!=0 or y%400==0)) and m==2 and d>28 or (y%4==0 and y%100!=0 or y%400==0) and m==2 and d>29:
    print('输入有误，请重新输入')
elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d>31:
    print('输入有误，请重新输入')
elif (m==4 or m==6 or m==9 or m==11) and d>30:
    print('输入有误，请重新输入')
else:
    a=y-2000
    sum=0
    b=0
    for i in range(2000,y):
        if i%4==0 and i%100!=0 or i%400==0:
            sum+=1
    if m==1:
        count=0
    elif m==2:
        count=31
    elif 2<m<8:
        for j in range(3,m):
            if j%2==1:
                 b+=31
            elif j%2==0:
                b+=30
        if y%4==0 and y%100!=0 or y%400==0:
            count=b+60
        else:
            count=b+59
    elif m>7:
        for k in range(8,m):
            if k%2==0:
                b+=31
            elif k%2==1:
                b+=30
        if y%4==0 and y%100!=0 or y%400==0:
            count=b+213
        else:
            count=b+212
    print('天数为:',a*365+sum+count+d,end=',')
    if (a*365+sum+count+d)%5==1 or (a*365+sum+count+d)%5==2 or (a*365+sum+count+d)==3:
        print('这天打鱼')
    else:
        print('这天晒网')
