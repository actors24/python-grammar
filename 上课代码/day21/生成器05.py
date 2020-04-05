
# 方式二： 函数 + yield
# def fn():
#     print(123)
#     return True
#     print(456)
# rst = fn()
#
# fn()

'''
def fn():
    print(1,'12行')
    yield
    print(2,'14行')
    yield
    print(3,'16行')

g = fn()
# print(rst)
next(g) #
next(g)
next(g)
'''
'''
def fn():
    print(1,'12行')
    yield 10
    print(2,'14行')
    yield 20
    print(3,'16行')
    yield  # return 后面没有数据 调用函数时， print(函数()) None

g = fn()
print(next(g))
print(next(g))
print(next(g))
'''


def fn():
    print(1,'12行')
    a = yield 10
    print('receving',a,'14行')
    b = yield 20
    print('receving',b,'16行')
    c = yield
    print('receving',c,'16行')

g = fn()
print(next(g))
g.send('孔夫子')

g.send('蒋浩楠')

g.send('嘉灵')


'''
总结：
    - 暂停
    - 返回 数据
    - 接收 数据  send() 类似next() 
'''