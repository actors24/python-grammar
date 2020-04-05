
# 1.直接创建
# dict1 = {'item1': '李浩', 'item2': '李浩同桌'}
# print(dict1)
# print(type(dict1))

# dict1 = {}
# print(dict1)
# print(type(dict1))

# 2.使用工厂函数
# dict1 = dict()
# print(dict1) # {}
# print(type(dict1)) #dict

# dict(mapping)
# dict1 = dict({'name':'剑飞','age':3,'hobbys':['打游戏','半夜上厕所','取向不详']})
# print(dict1) # {'name': '剑飞', 'age': 3, 'hobbys': ['打游戏', '半夜上厕所', '取向不详']}
# print(type(dict1)) #dict

# dict(**kwargs)
# dict1 = dict(one=1,two=2,name='国际广',addr='沙河')
# print(dict1) # {'one': 1, 'two': 2, 'name': '国际广', 'addr': '沙河'}


# dict(iterable)
# dict1 = dict([10,20,True,'123'])
# dict1 = dict(['16', '48'])
# dict1 = dict([('name','193'),('date','11-9')])
# dict1 = dict([['name','193'],['date','11-9']])
# dict1 = dict([range(2)])
# print(dict1) # {'1': '2', '4': '5'}  {'name': '193', 'date': '11-9'}
#
# #
# print(range(2))
# list1 = [range(2),range(2),range(1,3)]
# print(len(list1)) # 1
# for i in range(2):
#     pass



# python 特殊 赋值方式
# a,b = 10,20
# print(a,b) # 10 20

# a,b = 'ab'
# print(a) # a
# print(b) # b

# 模拟 实现 dict(iterable)
d1 = {}  # 创建 空字典
list1 = ['12','34']
for i in list1:
    print(i)  # i = '12'  '34'
# 给 空字典 添加 键值对
for a,b in list1:
    print(a,b)  # a,b = '12' a='1' b='2'     a,b='34'  a='3' b='4'
    d1[a] = b  # 给 字典 添加数据 键值对
print(d1) # {'1':'2','3':'4'}
