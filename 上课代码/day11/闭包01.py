
# 外层函数返回的 函数
# 持有其外层函数的局部变量 的  函数
# def outer():
#     a = 10
#     print(a)
#     #
#     def inner(value):
#         # print(a)
#         nonlocal a
#         a = value
#         return a
#     return inner
# # 函数调用 函数名()
# # 返回 函数
# fn = outer()
# print(fn('123'))


# 应用场景二
def outer():
    l1 = []
    for i in range(5):
        print(i,'24行')

        def inner():
            print(i,'26行')
            return i * 10
        l1.append(inner)
    return l1
rst = outer()
for fn in rst:
    print(fn())


def outer():
    l1 = []
    for i in range(5):
        print(i, '24行') # i=0 1
        # 方案一：for循环内部 声明inner函数使用默认参数，a = i,通过变量a保存每次循环i值
        def inner(a=i): # def inner(a=0):  def inner(a=1): def inner(a=2): def inner(a=3):
            print(a, '26行')
            return a * 10
        # 方案二：可以在for循环内部直接调用inner函数
        # inner()
        l1.append(inner)
    return l1


rst = outer()
for fn in rst:
    print(fn())




# 涉及知识点
# 1.函数声明在先，但是 调用在后
# 2.inner函数 在for循环完毕之后才做的调用
# 学会打断点 监听流程 来去理解
# 扩展：如何避免掉这种情况？两种解决方法，供参考
