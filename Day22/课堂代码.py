# 推导式
# 列表推导式
# l = [i for i in range(5) if i % 2 == 0]
# print(l)
#
# l = [i+1 for i in range(5) if i % 2 == 0]
# print(l)

# 函数
# def fn(num):
#     rst = num * 2
#     return rst
#
#
# l = [fn(i) for i in range(5) if i % 2 == 0]
# print(l)

# 匿名函数
# l = [(lambda x:x*2)(i) for i in range(5) if i % 2 == 0]
# print(l)

# l = [i for i in range(int(input('请输入一个数:')))]
# print(l)

# l = lambda n:[i for i in range(1,n+1)]
#
# print(l(5))

# 字典推导式
# d1={k:v for k,v in ['12','34']}
# print(d1)
#
# d1={v:k for k,v in ['12','34']}
# print(d1)

# d1={k+2:None for k in range(5)}
# print(d1)

# 集合推导式
# s1={i for i in range(5)}
# print(s1)

# 深浅拷贝
# 普通赋值
# a = 10
# b = a
# print(a, b)
# print(id(a), id(b))
#
# l1 = [1, 2, 3]
# l2 = l1
# print(id(l1), id(l2))
# l1[0] = 100
# print(id(l1), id(l2))

# 浅拷贝
# l1=[1,2,3]
# l2=l1.copy()
#
# print(l1,l2)
# print(id(l1),id(l2))
#
# l1[0]=100
# print(l1,l2)
# print()

# l1=[1,2,3,[4,5],[6,7]]
# l2=l1.copy()
#
# l1[3][0]=400
# print(l1,l2)

# 深拷贝
# l1=[1,2,3,[4,5],[6,7]]
# import copy
# l2=copy.deepcopy(l1)
#
# l1[3][0]=400
# print(l1,l2)
# print(id(l1),id(l2))

# l1=[1,2,3,[4,5]]
# l2=l1[:]
# print(l1,l2)

# __new__

# class A:
#     def __init__(self, name):
#         print('__init__')
#         self.name = name
#         print(name)
#
#     def __new__(cls, name):
#         print('__new__')
#         print(name)
#         return super().__new__(cls)
#
#
# a = A('jialing')


# str

# class A:
#     def __init__(self,s):
#         self.s=s
#
#     def __str__(self):
#         print('__str__')
#         return self.s
#
#
# a=A('sfdasd')
# print(a)

# call
# class A:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#         self.fn()
#
#
# def f():
#     print('我是fa函数')
#
#
# a = A(f)
#
# a()  # 实例对象被当作函数调用,会触发call方法

# call
# class A:
#     def __init__(self):
#         print('__init__')
#
#     def __del__(self):
#         print('__del__')
#
#
# a = A()
# b = a
# del a
# del b
# print('the end')

# class A:
#     def aaa(self):
#         print('sdfad')
#
#     @classmethod
#     def bbb(cls):
#         print('sdfsdfsdfad')
#
#     @staticmethod
#     def ccc():
#         print('rgbdvef')
#
#
# A.bbb()
# a = A()
# a.bbb()
# a = A()
# a.aaa()
# a.ccc()
# A.ccc()
# a.ccc()
