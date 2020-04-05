# #闭包
# #外层函数返回的函数
# def outer():
#     a=10
#     print(a)
#     def inner(value):
#         nonlocal a
#         a=value
#         return a
#     return inner
#
#
# fn=outer()
# print(fn('123'))

#应用场景二
# def outer():
#     l1=[]
#     for i in range(5):
#         print(i,'24行')
#         def inner():
#             print(i,'26行')
#             return i*10
#         l1.append(inner)
#     return l1
# rst=outer()
# for fn in rst:
#     print(fn())

# def outer():
#     l1=[]
#     for i in range(5):
#         print(i,'33行')
#         def inner(a=i):
#             print(a,'35行')
#             return a*10
#         l1.append(inner)
#     return l1
#
#
# rst=outer()
# for fn in rst:
#     print(fn())

#高阶函数
#1.filter
# rst=filter(None,[10,20,0,-1,False,'',True])
# print(rst)
# for i in rst:
#     print(i)
# print(list(rst))

#声明一个函数
# def fn(x):
#     if x%2==0:
#         return True
#     return False
#
#
# rst=filter(fn,[10,20,0,11,-1,False,'',None,True])
# rst=filter(fn,[10,20,0,11,-1,False,True])
# print(rst)
# print(list(rst))

#使用匿名函数来传参
# rst=filter(lambda x:True if x%2==0 else False,[10,20,0,11,-1,False,True])
# rst=filter(lambda x:x%2==0,[10,20,0,11,-1,False,True])
# print(rst)
# print(list(rst))

#2.map
# def fn(x,y,z):
#     return x+y+z
#
#
# rst=map(fn,[10,20,30],[40,50,60])
# print(rst)
# print(list(rst))
#
# rst=map(fn,[10,20,23],[40,50])
# print(rst)
# print(list(rst))
#
# rst=map(fn,[10,20,30],[40,50,60],[70,80,90])
# print(rst)
# print(list(rst))

#3.reduce
# import functools
# rst=functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
# print(rst)
#
# rst=functools.reduce(lambda x,y:x+y,[1,2,3,4,5],10)
# print(rst)
#
# rst=functools.reduce(lambda x,y:x+y,[],10)
# print(rst)

# #匿名函数\
# #调用该方式一
# fn=lambda x:x
# print(fn(10))
#
# #调用方式二
# print((lambda x:x)(120))
