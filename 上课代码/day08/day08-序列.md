## day08-序列

复习

~~~python
列表 元组 字符串  
	- 可迭代对象 for循环
    - 有下标 
    - 支持切片
序列： 有下标 + 支持切片 的数据类型 

可迭代对象 不一定是 序列
序列 一定是 可迭代对象
~~~

相关方法

~~~python
1.list(iterable)
	- 功能：把 iterable 转换 为 列表
    list('123')  # ['1','2','3']
    list([1,2,3]) # [1,2,3]
    list((10,20,30)) # [10,20,30]
2.tuple(iterable)
	- 功能：把 iterable 转换为 元组
3.str(obj)
	- 功能：任何对象 都可以转换为 字符串
4.len(obj)
	- 功能：返回 对象的 长度  
5.sum(iterable,start=0)
	- 功能：求和
    - 从0 开始，依次与 可迭代对象中每个元素相加累积求和
    demo：
        print(sum([10,20,30],40)) # 100
        print(sum((10,20,30))) #
        print(sum(range(5))) #
        # print(sum('123',start=0)) #
6.max()
	- 功能：求最大值
    - 方式一：
    	- max(iterable)
        print(max([10,20,30])) #30
        # print(max([10,20,30,-10,'abc'])) #30
        print(max((10,20,3))) # 20
        print(max(range(5))) # 4
        print(max('abc123')) # c
    - 方式二： argument参数
    	- max(arg1,arg2,arg3....) 直接把要比较的数据传入，逗号隔开即可
        a = 10
		b = 20
        print(max(a,b)) # 40
        
7.min()
	- 功能：求最小值
    - 使用方式 同上max()
    print(min(10,20,-10,0)) # -10
    print(min([10,20,-10,0])) # -10
    print(min((10,20,-10,0))) # -10
    print(min('abc,.123')) # ,
    print(min(range(5))) # 0
8.reversed(iterable)
	- 功能: 把可迭代对象中元素 进行翻转，形成一个 iterator object迭代器对象   （iterator object 可以实现for循环）
    demo：
        # reverse() 列表常用方法 列表.reverse()
        # 返回值：reverseiterator object  可迭代对象
        # rst = reversed([10,20,10,7])
        # rst = reversed((10,20,10,7))
        # rst = reversed('123')
        rst = reversed(range(5))
        print(list(rst)) # [7, 10, 20, 10]
        # for i in rst:
        #     print(i)

9.sorted(iterable,key=None,reverse=False)
	- 功能：把 iterable中元素 实现大小排序。默认升序
    - 参数
    	- iterable: 可迭代对象
        - key：排序方法
        - reverse: 升序/降序 默认False为升序
10.zip(iterable1,iterable2....) 压缩 打包
	- 功能：把 iterable1，iterable2，。。。进行压缩打包，形成一个zip对象。对象中元素-元组。元组中元素-每个iterable中对应下标元素构成。元组的个数 是由 最短的iterable 决定。
    # 返回值：zip object
    # rst = zip([10,20,30],[40,50,60],[70,80])
    # rst = zip([10,20,30],(40,50,60),[70,80])
    # rst = zip([10,20,30],'123',[70,80])
    rst = zip([10,20,30],range(3),[70,80])
    print(list(rst)) # [(10,), (20,), (30,)]   [(10, 40), (20, 50), (30, 60)]
11.enumerate(iterable,[start]) 枚举
	- 功能：把 iterable元素 进行枚举 形成一个enumerate对象。
    对象-可迭代对象。元素-元组  元组中元素-成对：元素-计数器，元素2-可迭代对象中每个元素
    - 参数
    	- iterable：可迭代对象
        - start： 计数器count。可选。 默认为0 
    demo：
        rst = enumerate([10,20,30],11)
    print(list(rst)) # [(11, 10), (12, 20), (13, 30)]

    rst = enumerate(range(5),11)
    print(list(rst)) # [(11, 0), (12, 1), (13, 2), (14, 3), (15, 4)]

    rst = enumerate('123',11)
    print(list(rst)) # [(11, '1'), (12, '2'), (13, '3')]

    rst = enumerate(('123',),11)
    print(list(rst)) # [(11, '123')]
~~~

