## day07

复习

~~~python、
元组 
	- 直接创建 (10,)
	- tuple(iterable)
元组常用方法
	- index() 查看元素对应的下标
	- count() 查看元素 次数    元素不存在，0
元组 特点
	- 不可变
	- 可迭代对象
	- 支持切片 支持索引
	- 存储多个数据，数据类型可以多种
列表 特点
	- 可迭代对象
	- 存储多个数据，数据类型可以多种
	- 支持切片 支持索引
	- 可修改 可变
二维列表
	- l = [10,20,[40]]
	- 访问二维列表内元素 l[2][0]
	- l[2][0] = 40
	- l[2].remove(40)
列表排序方法
	- 冒泡 
	- 选择排序
		- l1 = [1,4,10,3,5,2]
		  n = len(l1) # 6
		  for i in range(1,n):
		  	for j in range(i,n):
		  		if l1[i - 1] > l1[j]:
		  			l1[i-1],l1[j] = l1[j],l1[i-1]
		print(l1)  
~~~

元组遍历

~~~python
元组 第一个元素访问 元组[0]
逐一访问每个元素 
for i in (10,20,30,10):
    print(i)
使用len() 下标
for i in range(len(t)):
    print(t[i])
~~~

元组 相关操作符

~~~python
1.+
	两个或多个元组 进行 +，元组中的元素进行合并 拼接，形成一个新元组，原 元组 不变
    t1 = (10,)
    t2 = ('hailong',18,True,'female')

    # 1.+
    print(t1 + t2) # (10, 'hailong', 18, True, 'female')
    print(t1) # (10,)
    print(t2) #('hailong', 18, True, 'female')
2.*
	元组 * int, 元组中元素会成倍进行重复拼接，形成一个新元组，原元组 不变。
    t1 = (10,)
    print(t1 * 3) # (10, 10, 10)
	print(t1) # (10,)
3.in / not in 成员
	判断 某个元素 是否存在于 元组中。返回值：True/False
    t2 = ('hailong',18,True,'female')
    print('hailong' in t2) # True
	print('hailong' not in t2) # False
4.比较运算符 逻辑运算符
	元组中元素要注意 数据类型一致，才能进行比较
    如果元素为 字符串，则 比较的是 每个字符的ASCII值
    
    t1 = (10,)
    t2 = (18,'hailong',True,'female')
    t3 = (9,10)
    print(t1 > t3) # True
    print(t1 > t2) # False
    t4 = (18,'xinzong',False)
    print(t2 > t4) # False
~~~

元组 切片

~~~python
类似 列表 
t1 = ('hailong',18,True,'female','haodi',19,'xiaofeng',21,'shandong')

# print(t1[1:5]) # (18, True, 'female', 'haodi')
print(t1[1:]) # (18, True, 'female', 'haodi', 19, 'xiaofeng', 21, 'shandong')
print(t1[:]) # ('hailong', 18, True, 'female', 'haodi', 19, 'xiaofeng', 21, 'shandong')
print(t1[::2]) #('hailong', True, 'haodi', 'xiaofeng', 'shandong')
print(t1[::-1]) #('shandong', 21, 'xiaofeng', 19, 'haodi', 'female', True, 18, 'hailong')
print(t1[-1:-5:-1]) #('shandong', 21, 'xiaofeng', 19)
print(t1[-5:-1]) #('haodi', 19, 'xiaofeng', 21)
print(t1)

~~~

元组 特点

~~~python
 可以保存多个数据，数据类型可以多种。
有序  下标/索引
支持切片
不可修改  不可变    元组一旦创建之后，元素修改？删除？增加元素？index() count() 操作元素？
可迭代对象  for循环
~~~

##### for else结构

~~~python
for - else 结构
基本应用：
	- for循环正常执行完毕之后，则会执行 else 内的代码块
    demo：
        for i in range(5):
            print(i)  # 0 1 2 3 4
        else:
            print('我是else代码块')
	- for循环被强制中断，break,则直接结束for-else结构，则不会执行else内代码块
    	demo:
            	for i in range(5):
                    print(i) # 0 1 2 3
                    if i == 4:
                        print('当前i为4')
                        break # break
                else:
                    print('我是else代码块')
        demo2:
            	# 100-200内所有的质数  断点 endpoint
                for i in range(100,201):  #
                    for j in range(2,int(i**0.5) +1):
                        if i % j == 0: 
                            print(i,'不是质数')
                            break
                    else:
                        print(i,'是质数') # 101
~~~























