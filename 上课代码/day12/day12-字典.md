## day12-字典

* 什么是字典？

~~~python
dict   全拼dictionary
对比 列表 元组 字符串：
	- 可迭代对象  for循环
    - 键值对形式  映射关系 
    - 无序   
    	(python3.6版本更新，重新实现字典，采用紧凑型排列键值对顺序，所以相较于3.5，键值对变为有序,但是又不可完全过度依赖。从而使内存占用减少)
    - 可修改
    - 字典中 键 是唯一，不可重复,数据类型-不可修改/不可变/可哈希
~~~

* 创建字典

~~~python
1.直接创建
	- {key1:val1,key2:val2,key3:val3....}
    - 语法规范：
    	- 键值对之间用 逗号隔开
        - 键值之间用 冒号给开
    - 特殊情况
    	dict1 = {}  # 创建 空字典
		print(dict1)
		print(type(dict1)) # dict
2.工厂函数
	- dict() # 生成一个空字典 {}
    - dict(mapping) # 生成字典(字典由mapping中键值对初始化完成)
    	dict({'name':'剑飞','age':3,'hobbys':['打游戏','半夜上厕所','取向不详']})
    - dict(**kwargs) # 生成字典
    	
        demo:
            dict1 = dict(one=1,two=2,name='国际广',addr='沙河')
     # {'one': 1, 'two': 2, 'name': '国际广', 'addr': '沙河'}
    - dict(iterable)
    	- 语法：可迭代中元素 必须有长度概念，长度为2
        dict1 = dict(['16', '48'])
        dict1 = dict([('name','193'),('date','11-9')])
        dict1 = dict([['name','193'],['date','11-9']])
        dict1 = dict([range(2)])
    补充：
    	d1 = {}  # 创建 空字典
		list1 = ['12','34']
        for a,b in list1:
               print(a,b)  
               d1[a] = b  
~~~

* 键值对操作

~~~python
1.访问
	- 语法规范： 字典名[键名]
    - 注意：如果键名不存在，则报错keyError
    
    # 键值对访问 访问 name键 值
    print(dict1['name'])
    print(dict1['age'])
    print(dict1['lunch'])
    # 如果键不存在，则直接报错keyError
    print(dict1['phonenumber']) # keyError
2.修改
	- 语法规范  字典名[键名] = new_value
    - 如果键不存在，则会直接 添加键值对
3.增加
	- 语法规范  字典名[键名] = value
    - 注意：如果增加的键值对，键名与原字典中键名相同，则 对原键值对中值 做 修改。
    因此：字典中 键 是唯一，不可重复
4.删除
	del 字典名[键名]
    demo:
    	del dict1['lunch']
~~~

* 字典 遍历

~~~python
for i in dict1:
    print(i) # i 键名


# 循环 键名 值
for k in dict1:
    print(k,dict1[k])
~~~

* 字典常用方法

~~~python
1.D.clear()
	- 功能：清空字典中键值对，形成一个空字典
    - 返回值： None
    - 原字典 改变 变为空
2.D.copy()
	- 功能：复制原字典，生成一个新的字典
    - 返回值： 新的字典
    - 原字典 不变
3.D.fromkeys(iterable,value=None)
	- 功能：生成一个新的字典 键-可迭代对象中每个元素。值-value参数
    - 参数：
    	- 参数一：可迭代对象
        - 参数二：生成的新字典中 每个键对应的值
    - 原字典 不变
4.D.get(key,[d])
	- 功能：查询 键值对。 查询某个key对应的值
    - 返回值：
    	- 如果 key 存在，则返回值为 其对应的值
        - 如果 key 不存在，则返回值为 参数d。（参数d默认为None）
    - 参数：
    	- 参数一：key 要查询指定键
        - 参数二： d。可选 默认为None。一旦键不存在，则返回值为 d参数
    - 原字典不变
5.D.items()
	- 功能： 获取字典所有的键值对  
    - 返回值： 一个 set-like 对象。可迭代对象 。对象的元素-元组，元组中2个元素（键与值）
6.D.keys()
	- 功能： 获取字典所有的键 
    - 返回值： 一个 set-like 对象。可迭代对象 。对象的元素-字典中 键
7.D.values()
	- 功能： 获取字典所有的值
    - 返回值： 一个 set-like 对象。可迭代对象 。对象的元素-字典中 值
8.D.pop(k,[d])
	- 功能：删除指定键值对
    - 返回值：
    	- 如果key存在，返回值为 对应的值
        - 如果key不存在
        	- 如果参数d有传实参，则返回d
            - 如果参数d没有传实参，则报错 keyError
    - 参数
    	- 参数一：要删除的键值对 键
        - 参数二：可选。
    - 原字典 改变
9.D.popitem()
	- 功能：随机删除某个键值对。针对python3.6，此方法默认删除最后一个键值对
    - 返回值： 2-tuple
   	- 注意：如果当前字典为空，则报错 keyError
10.D.setdefault(k,[d])
	- 功能：
    	- 查看指定键值对 ，类似 get() 
        - 如果键不存在，则会进行字典 数据添加
    - 返回值：
    	- 如果key 存在，则返回值为 对应的值
        - 如果key 不存在，则返回值为 d。d默认为None
    - key存在，原字典不变；key不存在，原字典改变
11.D.update()
	- 功能： 更新 字典
    - 返回值： None
    - 原字典改变
    demo:
            dict1 = {'name':'海龙','age':18,'lunch':'noodles',1:[10,20,30],False:None,'12':12}
    # rst = dict1.update({'name':'海龙1','性别':'不详'})
    # rst = dict1.update(['12','34','56'])
    rst = dict1.update(name='善杰',age=20,hobbys=['吃饭','睡觉','学python'])
    print(rst) # None
    print(dict1)
~~~



























