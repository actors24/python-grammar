

'''
filter()
map()
reduce()
'''

# 1.filter()
# 生成 filter对象  迭代器对象
# rst = filter(None,[10,20,0,11,-1,False,'',None,True])
# print(rst)
# for i in rst:
#     print(i)
# print(list(rst)) # [10, 20, 11, -1, True]


# 声明一个函数
# def fn(x):
#     if x % 2 == 0:  # x 转为bool True
#         return True
#     else:
#         return False
# rst = filter(fn,[10,20,0,11,-1,False,'',None,True])
# rst = filter(fn,[10,20,0,11,-1,False,True])
# print(rst)
# print(list(rst)) # [10, 20, 11, -1, True] [10, 20, 0, False]

# 使用 匿名函数 来传参
# # rst = filter(lambda x: True if x % 2 == 0 else False,[10,20,0,11,-1,False,True])
# rst = filter(lambda x: x % 2 == 0,[10,20,0,11,-1,False,True])
# print(rst)
# print(list(rst)) # [10, 20, 0, False]



# 2.map()   map 地图  mapping 映射
def fn(x,y,z):
    return x + y + z

# rst  = map(fn,[10,20,30],[40,50,60])
# print(rst) # map object
# print(list(rst)) # [50, 70, 90]

# rst  = map(fn,[10,20,30],[40,50])
# print(rst) # map object
# print(list(rst)) # [50, 70]
#
# rst  = map(fn,[10,20,30],[40,50,60],[70,80,90])
# print(rst) # map object
# print(list(rst)) # [120, 150, 180]


# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
import functools
# rst = functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# print(rst) # 15

# rst = functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5],10)
# print(rst) # 25

rst = functools.reduce(lambda x, y: x+y,[],10)
print(rst) # 25