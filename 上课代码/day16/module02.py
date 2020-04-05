
# 想 使用 a.py 模块  A类

# functools 内置模块  .py   内容：reduce()
# import functools
# functools.reduce()







import a  # 等同于 给 变量a 重新赋值 a.py

print(a)  #  module 模块 a.py

print(a.a) # 10

print(a)


a = 20

print(a,'14行')  # 20

import a

print(a.a)


def fn():
    print('我是module02中fn')
fn()

a.fn()

'''
import module01   # 导入自定义模块
# 使用该模块中的内容 语法规范 点语法 类似 属性访问

# 使用模块中A
a = module01.A()
print(a.name) # module01_A
a.a_fn() # 我是class A中的a方法
# a.__chenxi()


# # 使用函数
# module01.fn() # 我是module01中的fn函数
#
# # 使用全局变量a
# print(module01.a) # 10

'''