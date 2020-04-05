# 递归
# def fn1():
#     print('今天天气真好')
#     fn1()
#
#
# fn1()

# 依次打印输出10到1
# def fn1(num):
#     if num==0:
#         return
#     print(num)
#     fn1(num-1)
#
#
# fn1(10)

# 阶乘
# def fn(num):
#     if num==1:
#         return 1
#     return num*fn(num-1)
#
#
# print(fn(5))

# 菲薄那窃数列
# def fn(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fn(n-1)+fn(n-2)
#
#
# print(fn(8))

# 作用域\
# 全局作用域
# a=10
# def fn1():
#     print(a)
#     b=20
#     print(b)
#
#
# fn1()

# 函数嵌套调用
# def fn1():
#     print('fn100')
#
#
# def fn2():
#     print('fn200')
#     fn1()
#
#
# fn2()
#
# a=5
# def fn3():
#     a=10
#     print(a,'64行')
#     def fn4():
#         print(a,'66行')
#     fn4()
# fn3()
# print(a,'69行')

# 使用global
# a=10
# def fn1():
#     global a
#     a+=10
#     print(a,id(a))
#
#
# fn1()

# def fn2():
#     global a
#     a=20
#     print(a)
# fn2()
# print(b)\

# c=100
# def fn3():
#     global c
#     c+=100
#     print(c)
#     def fn4():
#         global c
#         c+=100
#         print(c)
#
#     fn4()
# fn3()
# print(c)

# nonlocal
def fn5():
    d=100
    print(d,'106行')
    def fn6():
        nonlocal d
        d+=100
        print(d)
        def fn7():
            nonlocal d
            d+=100
            print(d)
        fn7()
    fn6()
    print(d,'117行')
fn5()

# 函数作为参数
# def fn1(fn):
#     print(fn,id(fn))
#     fn()
#
#
# def fn2():
#     print('我太开心啦')
#
#
# fn1(fn2)
# print(fn2,id(fn2))

# 重载
# def fn1(name):
#     print('我叫',name)
#
#
# def fn1(name,age):
#     print(f'我叫{name},我今年{age}岁了')
#
#
# fn1('嘉灵',22)

# 匿名函数
# a=lambda x:x+2
# print(a)
# print(a(10))

# b=lambda : 10+20
# print(b())
# print((lambda : 10+20)())
