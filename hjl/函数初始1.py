# def fun(a,b=0):
#     sums=0
#     for i in a:
#         b+=i
#     print(b)
#
#
# fun([1,2,3],10)

# def fun2(a,b=10):
#     return a,b
#
#
# print(fun2(18,12))

# def fun1(n):
#     if n > 0:
#         print('今天吃什么')
#         fun1(n - 1)
#
#
# fun1(20)


# def fun2(num):
#     if num==1:
#         return 1
#     return num * fun2(num-1)
#
#
# print(fun2(5))

# def fun3(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fun3(n-1)+fun3(n-2)
#
# print(fun3(8))


# def fun3():
#     a=10
#     print(a,'//')
#     def fun4():
#         a=20
#         print(a,'fn4')
#     fun4()
# fun3()

# 全局变量
# a = 10
#
#
# def fn1():
#     global a
#     a += 10
#     return a
#
#
# print(a)
# print(fn1())
a = 0


# def fb2():
#     global a
#     a = 10
#     print(a, id(a))
#
#     def fb3():
#         global a
#         a += 10
#         print(a, id(a))
#
#     fb3()
# print(a)
#
# fb2()
# nonlocal
# b=0
# def fun():
#     a=10
#     print(a,id(a))
#     def fun2():
#         nonlocal a
#         global b
#         for i in range(6):
#             a+=10
#             b+=10
#             print(a,b,id(a))
#         def fun3():
#             nonlocal a
#             a*=10
#             print(a)
#
#         fun3()
#     fun2()
# fun()
# 函数重载1
# def fun1(a,b):
#     print(a,b)
#
# def fun1(a):
#      print(a)
#
# fun1(1,2)\

# 匿名函数
# # a=lambda x:x+2 if 1>0 else x
# # print(a(1))
# print((lambda x:x+1 if 1==0 else x)(2))

# def outer():
#     a = 1
#     print(a)
#
#     def inner(b):
#         a = b
#         print(a)
#         return a
#
#
# print(outer())

# def outer():
#     l1=[]
#     for i in range(5):
#         print(i,'130行')
#         def inner(a=i):
#             print(a,'132行')
#             return i*10
#         l1.append(inner)
#     return l1
# rst=outer()
# for fn in rst:
#     print(fn())

# import re
# print(re.match('www','www.baidu.com').span())
# print(re.search('com','www.baidu.com').span())

import functools
print(list(functools.reduce(lambda x,y:x+y,[1,2,3],10)))