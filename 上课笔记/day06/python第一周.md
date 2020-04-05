python第一周

1.变量命名规则   标识符命名规范

2.分支结构  if / if else 、 if elif...else      if嵌套   

3.循环结构？while for 语法规范

while 布尔表达式：

​	代码块 循环体

for 变量 in 可迭代对象:

​	代码块 循环体

4.循环 列表

​	for i in l:

​		print(i)

​	for i in range(len(l)):  len(l)-列表长度  4 range(4)-0-3

​		print(l[i])

5.1-100内奇数  6个一行

6.倒序-降序

​	冒泡排序  选择排序

复习

- 列表创建
  - 直接创建
    - [1,2,3,4]
  - 工厂函数list()
    - list(range(1,5)) list('1234')-['1','2','3','4'] list([1,2,3,4])
- 列表元素增删改查
  - 列表[len(列表)-1] 最后一个元素
  -  del 列表[index]
  - 列表[len(列表)-1] = newvalue
  - 不能手动增加元素
- 列表 遍历
- 列表方法
  - append() 给列表末尾追加一个元素
  - extend(iterable) 给列表末尾追加 可迭代对象中每个元素
  - insert(index,value) 在索引之前插入一个元素 
  - clear() 清空所有元素  空列表
  - remove(val) 删除指定元素
  - pop(index) 删除某个元素 默认删除最后一个元素
  - reverse() 翻转  倒序 
  - count(val) 统计次数  >= 0
  - index() 查询指定元素 对应的下标
  - copy() 浅拷贝 新列表
  - sort() 实现 元素大小排序
- 切片
  - 列表[start:stop:step]
  - 列表[0:5] 
  - 列表[:5]  列表[:]  列表[::-1]  列表[-5:-1]
- 排序
  - 冒泡排序
  - 选择排序