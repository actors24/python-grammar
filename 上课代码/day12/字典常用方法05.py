
# 1.clear()
# dict1 = {'name':'海龙','age':18,'lunch':'noodles','name':'肖枫'}

# rst = dict1.clear()
# print(rst) # None
# print(dict1) # {}空字典

# 2.copy()
# rst = dict1.copy()
# print(rst)
# print(dict1)

# 3.fromkeys()
# dict1 = {'name':'海龙','age':18,'lunch':'noodles','name':'肖枫'}
# rst = dict1.fromkeys([10,20,30,40],'193')
# print(rst) # {10: None, 20: None, 30: None, 40: None}  {10: '193', 20: '193', 30: '193', 40: '193'}
# print(dict1)

# 4.get() 访问 查询
# dict1 = {'name':'海龙','age':18,'lunch':'noodles'}

# rst = dict1.get('name','没找到')
# rst = dict1.get('name')
# print(dict1['name1'])
# print(rst) # None
# print(dict1)

# 5. items() keys() values()  a set-like object
# dict1 = {'name':'海龙','age':18,'lunch':'noodles'}
# rst1 = dict1.items()
# print(rst1)
# print(list(rst1)) # [('name', '海龙'), ('age', 18), ('lunch', 'noodles')]
# rst2 = dict1.keys()
# print(rst2)
# print(list(rst2)) # ['name', 'age', 'lunch']
# rst3 = dict1.values()
# print(rst3)
# print(list(rst3)) # ['海龙', 18, 'noodles']

#6.pop()
# dict1 = {'name':'海龙','age':18,'lunch':'noodles'}

# rst = dict1.pop('name1','没找到啊！')
# print(rst) # 海龙
# print(dict1) # {'age': 18, 'lunch': 'noodles'}

# 7.popitem()
# dict1 = {'name':'海龙','age':18,'lunch':'noodles',1:[10,20,30],False:None,'12':12}
# dict1 = {}
# rst = dict1.popitem()
# print(rst) # ('lunch', 'noodles')  2-tuple
# print(dict1)

# 8.setdefault()
# dict1 = {'name':'海龙','age':18,'lunch':'noodles',1:[10,20,30],False:None,'12':12}
# rst1 = dict1.setdefault('name1','蒋浩楠')
# print(rst1) # get() None
# print(dict1)

# 9.update()
dict1 = {'name':'海龙','age':18,'lunch':'noodles',1:[10,20,30],False:None,'12':12}
# rst = dict1.update({'name':'海龙1','性别':'不详'})
# rst = dict1.update(['12','34','56'])
rst = dict1.update(name='善杰',age=20,hobbys=['吃饭','睡觉','学python'])
print(rst) # None
print(dict1)