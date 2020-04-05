## 列表

##### 二维列表

~~~python
二维列表： 列表 嵌套列表
多维列表
list1 = [10,20,[30,40]]
list2 = [
    [10,20,30,40],
    [10,20,30,40],
    [10,20,30,40],
    [10,20,30,40]
	]
~~~

列表元素访问

~~~python
list1 = [10,20,[30,40]]
列表[下标] list1[2][0]
~~~

列表遍历循环

~~~python
list1 = [10,20,[30,40]]
for i in list1:
    
##    if type(i) == list:
    if isinstance(i,list) == True:
        for j in i:
            print(j)
    else:
        print(i)
~~~

列表相关操作符

~~~python
1. +
	两个列表通过+进行运算，可以实现的 两个列表中元素 拼接，形成一个新的列表。原列表没有影响
    list1 = [1,2,3]
    list2 = [4,5,6]
    print(list1 + list2) # [1, 2, 3, 4, 5, 6]
    print(list1)
    print(list2)
    print(list1 + [10]) # [1, 2, 3, 10]
2. *
	同一个列表*整型数字，可以实现 原列表中元素进行成倍的拼接，形成一个新的列表。原列表没有影响
    print([1,2,3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
3. in / not in 成员运算符
	判断某个元素 是否存在于 列表中
    print(3 in [1,2,3]) # True
	print(3 not in [1,2,3]) # False
    补充：
    	## 判断一下 某个元素是否存在于列表中？
        ## 1.使用 in not in
        ## 2.使用for循环 逐一进行判断
        ## 3. 列表常用方法 count()  (也可考虑 index() remove())
4.比较运算符 > < >= <= != ==  逻辑运算符
	 列表中元素进行一一比较，一旦比较出大小，则停止
 	列表中元素数据类型要一致，否则比较会报错，typeError
    
    demo：
        list1 = [1,2,3]
        list2 = [4,5,6]
        print(list1 > list2) # False
        
        list3 = [10,'abc',True]
        list4 = ['ef',12,False]
        print(list3 > list4)
        
        list3 = [10,11]
        list4 = [9.5,12]
        print(list3 > list4)
        
        list3 = ['ab','ec','df']
        list4 = ['ef','ac','bd']
        print(list3 > list4 and list3 < list4)
~~~

#### 总结

~~~python
列表 特点：
	- 可迭代对象 for使用
    - 元素的数据类型没有限制
    - 有 下标/索引
    - 支持 切片
    - 可修改  增加 删除 修改
有序的数据集合 
~~~

### 元组 tuple

~~~python
类似 列表
保存多个数据
	- 元素数据类型 可以多种
    - 不可修改 
~~~

创建方式

~~~python
1.直接创建
	- (10,30,True,'abc')
    - 括号可以省略，但是 逗号不能省
    	- t1 = 10,20,30  # (10,20,30)元组
        - t1 = 10,    #（10，）元组
    - t = (10,)
    	- 注意：如果元组中只有一个元素，切记，元素末尾 加逗号
   		- t = （10）  # 10  int  
2.工厂函数
	- tuple()  空元组
    - tuple(iterable)
    	## 可迭代对象 str list range tuple
        t1 = tuple('wanghailong')
        # ('w', 'a', 'n', 'g', 'h', 'a', 'i', 'l', 'o', 'n', 'g')
        t1 = tuple(['leige','shanjie'])
         # ('leige', 'shanjie')
        t1 = tuple(range(5))
        # (0, 1, 2, 3, 4)
        t1 = tuple((10,20,30))
        ## (10, 20, 30)
        print(t1)
~~~

元组元素 操作 增删改查

~~~python
1.查 访问
	- 语法规范
		元组[index] 
2.修改
	无法修改
3.删除
	无法删除
4.增加
	无法增加
~~~

元组常用方法

~~~python
1.T.count(value)
	- 功能：统计 value 在元组中 出现的次数
    - 返回值： >= 0 整数
    	- 如果value 出现在元组中，返回值 >0 整数
        - 如果value不存在，则 返回值0
    - 原 元组 没有改变
2.T.index(value,[start,[stop]])
	- 功能：查询 指定value 在 元组中的 下标/位置
    - 返回值： int
    	- 如果value存在，返回的是第一次出现的index
        - 如果value不存在，报错valueError
    - 参数
    	- start：可省略，默认为0。
        		- 查找 起始下标 并包含该位置
        - stop：可省略，默认到 最大下标(末尾)
        		- 查找 结束下标 不包含该位置
~~~





