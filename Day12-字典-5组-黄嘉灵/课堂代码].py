# 字典创建
# 1.直接创建
# dict1 = {'name': '黄嘉灵', 'age': 22, 'id': 45156514}
# print(dict1,type(dict1))
# print(dict1['name'])

# 2.使用工厂函数
# #dict(**kwargs)
# dict1=dict(name='黄嘉灵',age=22,id=5465)
# #dict(mapping)
# dict2=dict({'name':'jialing','age':22,'id':1564})
# print(dict1)
# print(dict2,type(dict2))
# print(dict1,type(dict1))

# dict(iterable)
# dict1=dict(['12','45'])
# dict2=dict([('name','192'),('date','111')])
# dict3=dict([range(2),(range(1,3))])
# # print(dict1)
# print(dict2)
# print(dict3)

# 模拟实现dict(iterable)
# d1=dict()   #创建空字典
# list1=['12','45']
# 给空字典添加键值对
# for a,b in list1:
#     print(a,b)
#     d1[a]=b    #给字典添加数据键值对
# print(d1)

# python特殊赋值方式
# a,b='12'
# print(a,b)

# 字典键值对操作
# dict1={'name':'jialing','age':18,'lunch':'noodles','name':'sf'}
#
# #键值对访问
# print(dict1['name'])
# print(dict1['age'])
# print(dict1['lunch'])
# #如果键不存在,则直接报错
# print(dict1['phonenumber'])

# 键值对修改
# dict1['lunch']='dumplins'
# print(dict1)
#
# #增加
# dict1['id']=45646
# print(dict1)
# dict1['id']=54654
# print(dict1)

# 删除
# del dict1['lunch']
# print(dict1)

# 字典遍历
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# #循环遍历
# for i in dict1:
#     print(i,dict1[i])

# dict1={'name':'jialing','age':18,'lunch':'noodles','hobbies':['学python','调bug'],1:True,True:None}
# # print(dict1)
# #
# # dict1['addr']=507
# # print(dict1)

# 字典键值对构成
# print({'123': '123'})
# print({123: 1234})
# print({123: True})
# print({123: [1, 2, 3]})
# print({True: (1, 2, 3)})
# # unhashable type hash哈希 列表-不可哈希的类型   可修改类型/可变
# # 总结:数据类型-列表 字典
# # 数据类型-int float str bool None 元组 复数
# # 字典中键有数据类型限制,必须是不可修改的数据类型 hashable type   可哈希类型
# print({(1, 2, 3): 10})


# 字典的常用方法
# 1.clear()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# dict1.clear()
# print(dict1)
#
# #2.copy()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# print(dict1.copy())

# 3.fromkeys()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst=dict1.fromkeys([10,20,30,40],'193')
# print(rst)
# print(dict1)

# 4.get()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst=dict1.get('name','没找到')
# print(rst)
# print(dict1)

# 5.items() key() value()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst1=dict1.items()
# print(rst1)
# print(list(rst1))
# rst2=dict1.keys()
# print(rst2)
# print(list(rst2))
# rst3=dict1.values()
# print(rst3)
# print(list(rst3))

# 6.pop()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst=dict1.pop('name1','没找到啊')
# print(rst)
# print(dict1)

# 7.popitem()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst=dict1.popitem()
# print(rst)
# print(dict1)

# 8.setdefault()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst1=dict1.setdefault('name1','xiaofeng')
# print(rst1)
# print(dict1)

# 9.update()
# dict1={'name':'jialing','age':18,'lunch':'noodles'}
# rst=dict1.update({'name':'hailong','xingbie':'buxiang'})
# rst=dict1.update(['12','34','56'])
# rst=dict1.update(name='删节',age=20,hobbies=['吃饭','睡觉','学python'])
# print(rst)
# print(dict1)

# 集合
# 直接创建
# set1={1,2,3,45,2,56,24,24,'dad',('dfgd',45)}
# set1=set([123.,24,25])
# print(set1,type(set1))

# 利用`工厂函数
# 1.set()
# set1=set()
# print(set1,type(set1))
#
# set1=set([12,32,True])
# print(set1,type(set1))

# #通过程序来实现去重
# list1=[1,2,3,4,1,2,3,4,4,3,2,1,5]
# new_list=[]
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# 集合方法
# 1.add()
# set1={1,2,3}
# rst=set1.add(5)
# rst=set1.add(2)
# print(rst)
# print(set1)

# 2.clear()
# set1={1,2,3}
# set1.clear()
# print(set1.clear())
# print(set1)

# 3.discard()
# set1={1,2,3}
# print(set1.discard(1))
# print(set1.discard(10))
# print(set1)

# 4.pop()
# set1={1,2,3,True,False,None}
# print(set1.pop())
# print(set1)

# 5.
# set1 = {1, 2, 3}
# print(set1.remove(1))
# print(set1)

#6.update()
# set1={1,2,3}
# print(set1.update({4,5,6},{7,8,9}))
# print(set1)

#7.difference()
# set1={1,2,3,5,6,7,8}
# print(set1.difference({0,1,2,3,4,5},{5,3,5,6}))
# print(set1)

#8.difference_update()
# set1={1,2,3,5,6,7,8}
# print(set1.difference_update({0,1,2,3,4,5},{5,3,5,6}))
# print(set1)

#intersection()
# set1={1,2,3,5,6,7,8}
# print(set1.intersection({0,1,2,3,4,5}))
# print(set1)

#union()
# set1={1,2,3,5,6,7,8}
# print(set1.union({0,1,2,3,4,5}))
# print(set1)