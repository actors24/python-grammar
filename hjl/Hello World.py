# def fun1(a):
#     def fun3():
#         def fun2():    #def fun2---创建fun2函数对象
#             nonlocal a
#             a+=1
#             return a
#         return fun2
#     return fun3#return 函数的调用   return 值（fun2对象）
# print(fun1(10)())
# fun1（） #---函数的调用
# fun1      #---函数对象     fun1---函数对象的首地址
# f=fun1()
# print(f())
# print(fun1()())

# a=1,2,3,4,5
# a[0:2]
# print(a[0:2])

# tp1 = "i am {}, age {}, {}".format("seven", 18, 'alex')
# tp2 = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
# tp3 = "i am {0}, age {1}, really {0}".format("seven", 18)
# tp4 = "i am {0}, age {1}, really {0}".format(*["seven", 18])
# tp5 = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
# tp6 = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
# tp7 = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
# tp8 = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
# tp9 = "i am {:s}, age {:d}".format(*["seven", 18])
# tp10 = "i am {name:s}, age {age:d}".format(name="seven", age=18)
# tp11 = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
# print(tp1)
# print(tp2)
# print(tp3)
# print(tp4)
# print(tp5)
# print(tp6)
# print(tp7)
# print(tp8)
# print(tp9)
# print(tp10)
# print(tp11)

# list1=[1,2,3,'hehe','大哥',bool,int,float,str,True,False,None,1405.22]
# print(list1)
# a=[1,323,24,'fjf']
# for i in a:
#     print(i)

# a='ggsgsg'
# for i in a:
#     print(i)

# a=[5,3,6,4,8,1,7,2]
# b=len(a)
# for i in range(b-1):
#     for j in range(b-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# a=[1,2,3]
# a.insert(0,a[len(a)-1])
# a.pop()
# print(a)

#螺旋填数
# while 1:
#     n=int(input('请输入一个整数\n'))
#     m=int(input('请输入一个整数\n'))
#     l=list()
#     l=[[0]*n for i in range(m)]
#     f='y'
#     row=0
#     list1=0
#     q=1
#     value=1
#
#     while value<=n*m:
#         if f=='y':
#             l[row][list1]=value
#             if list1>=n-q:
#                 f='x'
#                 continue
#             list1+=1
#         if f=='x':
#             l[row][list1]=value
#             if row>=m-q:
#                 f='z'
#                 continue
#             row+=1
#         if f=='z':
#             l[row][list1]=value
#             if list1<=q-1:
#                 f='s'
#                 continue
#             list1-=1
#         if f=='s':
#             l[row][list1]=value
#             if row-1<=q:
#                 f='y'
#                 q+=1
#             row-=1
#         value+=1
#     for r in l:
#         print(r)

#最大公约数
# a=int(input('aa'))
# b=int(input('bb'))
# c=0
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         c=i
# print(c)


# def abc():
#     sums=0
#     def abd():
#         nonlocal sums
#         sums+=1
#         return sums
#     return abd
# def abe():
#     a=abc()
#     print(a())
#     print(a())
#     print(a())
#
# abe()
#调用内部函数
# def hello():
#     print('hello world')
#     def inside():
#         print('hello python')
#     return(inside)
# a=hello()
# a()

# def hello():
# #     var=5
# #     def inside():
# #         print(var)
# #         var=3
# #     inside()
# # hello()

# def funout():
#     def funIn():
#         print('Bingo,you have been successfully accessed me!')
#     funIn()
# funout()

# abc = 100
# sum1 = 1
# sum2 = 1
# sum3 = 1
# while abc < 1000:
#     c = abc % 10
#     b = abc // 10 % 10
#     a = abc // 100
#     for i in range(1, c + 1):
#         sum1 *= i
#     for j in range(1, b + 1):
#         sum2 *= j
#     for k in range(1, a + 1):
#         sum3 *= k
#     if sum1 + sum2 + sum3 == abc:
#         print(abc, end=' ')
#     abc += 1

m=int(input('请输入一个数字：'))
for i in range(m+1):
    if isinstance(i**0.5,int)==True:
        print(i)