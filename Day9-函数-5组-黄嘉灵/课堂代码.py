# # 函数
# def star(num, symbol, s):
#     print(s)
#     for i in range(num):
#         print(symbol, end='')
#     print()
#
#
# star(20, '_', '窗前明月光')
# star(30, '%', '疑是地上霜')
# star(40, '$', '天王盖地虎')
# star(50, '#', '小鸡炖蘑菇')


# 函数参数
# def fn1():
#     print('我是fn1函数')
#
#
# def intro(name, age):
#     print(f'我叫{name},我今年{age}岁了')


# # 调用
# ## 位置参数
# intro('卫东', 22)
# intro('肖峰', 11)
# intro('鑫总', 33)
#
# # 关键字参数
# intro(name='卫东', age=22)
# intro(name=18,age='鑫总')
#
# # 混用
# intro('卫东',age=18)
# intro(age=18,'卫东')   # 错误

# # 默认参数
# def intro(name,age=18):
#     print(f'我叫{name},我今年{age}岁了')
#
#
# intro('小飞飞',18)
# intro('小飞飞',19)
# intro(age=20,name='小飞飞')

# 可变长参数
# def fn2(*args):
#     print(args)
#     for i in args:
#         print(i)
#
#
# # 调用
# fn2(10)
# fn2(10,20,30,40,50)

# # **kwargs
# def fn3(**kwargs):
#     print(kwargs)
#     for i in kwargs:
#         print(i)
#
#
# fn3(name='鑫总',age=18,addr='沙河')

# # demo
# def my_intro(name,age=18,*hobbies,**others):
#     print(name,age)
#     print(hobbies)
#     print(others)
#
#
# my_intro('黄嘉灵',22,'打篮球','打台球',other1='看电视',others2='去玩游戏')

# return
# def fn1():
#     print('江公子准备去烫头了')
#     return
#     print('萧公子给他送烟去了')
#
#
# fn1()

# #函数return 返回值
# def fn2():
#     return '蒋浩南你干嘛呢'
#     return  10
#     return [10,20,30,40]
#     return (10,20,420)
#     return range(10)
#     return 10+20
#     return True
#
#
# rst = fn2()
# print(rst)
# print(type(rst))

# # 返回值None
# def fn3():
#     print('我是善杰')
#     return None
#
#
# rst1 = fn3()
# print(rst1)

# # 模拟sum求和
# def sums(a,b=0):
#     for i in a:
#         b+=i
#     return b
#
#
# print(sums([1,2,3],10))

# def fn4():
#     print('我是fn4')
#     return True
#
#
# def fn5():
#     print('我是fn5')
#     rst = fn4()
#     if rst == True:
#         print('今晚没作业')
#
#
# fn4()
# fn5()
