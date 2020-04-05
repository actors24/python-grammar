# def fn1(y):
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         return True
#     else:
#         return False
#
#
# def fn2(y, m, d):
#     if m in [1, 3, 5, 7, 8, 10, 12] and 0 < d <= 31:
#         return True
#     elif m in [4, 6, 9, 11] and 0 < d <= 30:
#         return True
#     elif m == 2 and (fn1(y) == True and 0 < d <= 29 or fn1(y) == False and 0 < d <= 28):
#         return True
#     else:
#         return False
#
#
# def fn3(y, m, d):
#     count = 0
#     b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if fn2(y, m, d):
#         for i in range(0, m - 1):
#             count += b[i]
#         if m > 2 and fn1(y) == True:
#             count += 1
#         count += d
#         print(f'{y}年{m}月{d}日是这年的第{count}天')
#     else:
#         print('日期不合法')
#
#
# fn3(1999, 3, 1)

# 1.1.避免代码冗余，提高代码的可重用性，提高代码的可维护性，提高代码的灵活性
# 2.形参是函数声明时定义的参数，实参是调用函数时往里传入的值
# 3.def
# 4.global
# 5.nonlocal
# 6.可以避免某个形参没有传入值或者实参的值没有传入对应的形参中
# 7.默认参数在函数声明形参时就赋值了，关键字参数是调用该函数时才在字面值前加入形参的变量名
# 8.对，因为return语句负责把输入的多个数据把包成元组
# 9.两个
# # 11.
# def fn1(x,y,a,b):
# 	return x*y+a*b
# 12.打印Hello World!
# 13.不能直接调用内部函数，要在内部函数下面调用该函数,然后再在外部调用外部函数
# 14.print(var)和var=3调换位置
# 17.  a = lambda x, y=3: x * y
# 18.
# def fun(x):
#     if x % 2 == 0:
#         return x
#     else:
#         return None

# 19.
# def fac():
#     m = int(input('请输入一个整数:'))
#     for i in range(1, m):
#         if m % i == 0:
#             print(i, end=' ')
#
#
# fac()

# 20.
# def hello_world(n):
#     for i in range(n):
#         print('HelloWorld')
#
#
# hello_world(10)

# 21.
# def fun(n):
#     sums = 0
#     while n != 0:
#         n //= 10
#         sums += 1
#     print('这个数是', sums, '位数')
#
#
# fun(123456)
