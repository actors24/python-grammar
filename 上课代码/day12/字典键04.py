
# dict1 = {'name':'海龙','age':18,'lunch':'noodles','hobbys':['学python','写python','调bug'],1:True,True:None}
#
# print(dict1)
#
# # 增加
# dict1['addr'] = 507
#
# print(dict1)

# 字典 键值对构成

print({'123':'123'})
print({123: 123})
print({123: True})
print({123: [1,2,3]})
print({True: (1,2,3)})
#  unhashable type   hash哈希  列表-不可哈希的类型   可修改类型/可变
# 总结：数据类型-列表 字典
# 数据类型-int float str bool None 元组 复数  不可修改
#  字典中 键 有数据类型限制。必须是 不可修改的数据类型  hashable type 可哈希类型
print({[1,2,3]: 10})