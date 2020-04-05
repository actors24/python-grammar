# #1.
# #打印输出1-100
# for i in range(1,101):
#     print(i,end=' ')
# print()
# #2.
# #倒序输出1-100
# for i in range(100,0,-1):
#     p+++++rint(i,end=' ')
# print()
# #3.
# #定义变量
# sums=0
# for i in range(1,101):
#     sums+=i
# #输出1-100的和
# print(sums)
#
# #4.
# #输出2-5的乘积
# print('2-5的乘积为：',2*3*4*5)
#
# #5.
# for i in range(1,101):
#     if i%3==0 and i%7==0:   #判断是否能同时整出3和7
#         #输出结果
#         print(i)
#
# #7.
# #打印输出100遍语句
# for i in range(1,101):
#    print('这是第',i,'遍输出','好好学习，天天向上，老实做人，不搞对象')
#
# #8.
# #定义两个变量,分别存储奇数和偶数的和
# sum1=0
# sum2=0
# for i in range(1,100,2):
#     sum1+=i
# #输出奇数的和
# print('奇数的和为:',sum1)
# for j in range(2,101,2):
#     sum2+=j
# #输出偶数的和
# print('偶数的和为:',sum2)
#
# #12.
# #定义一个累加器,用于存放一行数据的个数
# count=0
# for i in range(20,81):
#     if i%3==0:      #满足条件打印
#         print(i,end=' ')
#         count+=1    #累加器加一
#         if count%5==0:  #数据每五个换行
#             print()
#
#
# #13.
# #定义变量
# i=25
# sums=0
# #人数不满100则继续循环
# while i<100:
#     i*=1.25
#     sums+=1
# #打印输出语句
# print('在'+str(2012+sums)+'年培训人数将达到100万人')
#
# #14.
# #输入两个数字
# m=int(input('请输入第一个数:\n'))
# n=int(input('请输入第二个数:\n'))
# #判断输入的数是否为正数
# if m<=0 or n<=0:
#     print('输入有误,请重新输入')
# #从m,n之间最小值开始倒序循环
# for i in range(min(m,n),0,-1):
#     if m%i==0 and n%i==0:   #满足最大公约数则输出并跳出循环
#         print('这两个数的最大公约数为:',i)
#         break
#
# #15.
# #输入两个数字
# m=int(input('请输入第一个数:\n'))
# n=int(input('请输入第二个数:\n'))
# #判断输入的数是否为正数
# if m<=0 or n<=0:
#     print('输入有误,请重新输入')
# else:
#     a=0
#     while 1:    #只要没找到最小公倍数则继续循环
#         a+=1
#         if a%m==0 and a%n==0:   #满足最小公倍数则输出
#             print('这两数的最小公倍数为:',a)
#             break
#
# #16.
# #从1,100循环遍历
# for i in range(1,101):
#     if i%7==0:  #打印能被7整除的数
#         print(i,end=' ')
# print()
#
# #17.
# 从100到200循环遍历
for i in range(100, 201):
    # i除了1的因子的范围为2到根号i
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:  # 如果i能被j整除则不满足条件,跳出当前循环
            break
    else:  # 打印满足质数的数字
        print(i, end=' ')
