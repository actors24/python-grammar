##list1 = [10,True,'good','afternoon',20.5]
## 修改 第二个元素
##list1[1] = False
##print(list1)

## 删除 第一个元素
##del list1[0]
##print(list1)

## 原来基础上 增加一个元素
##list1[5] = 100
##print(list1[10])
 

## 查看元素
##print(list1[0])
##print(list1[1])
##print(list1[2])
##print(list1[3])
##print(list1[4])
## 逐一打印每个元素
##for i in range(0,len(list1)):
##    print(list1[i])

##for i in list1:
##    print(i)


## 切片  访问某一区间范围内的元素
list1 = [10,True,'good','afternoon',20.5]
print(list1[0:4]) # [10, True, 'good', 'afternoon']
print(list1[:4])  # range(10) 起始值可省略，默认从0开始
print(list1[1:4]) # [True, 'good', 'afternoon']
print(list1[1:])  # [True, 'good', 'afternoon', 20.5] 结束值也可省略，默认切片到最后一个元素
print(list1[:])  # [10, True, 'good', 'afternoon', 20.5]
print(list1[0:4:2]) # :2 步长
print(list1[0:4:-1]) # [] 一旦截取不到元素，返回空列表
print(list1[4:0:-1]) # [20.5, 'afternoon', 'good', True]
print(list1[4:-1:-1]) # []
print(list1[::-1]) #[20.5, 'afternoon', 'good', True, 10]
print(list1[0:10]) # [10, True, 'good', 'afternoon', 20.5]
print(list1[2:2]) # []
print(list1[-3:-1:1]) # ['good', 'afternoon']
print(list1[-1:-3:-1]) # [20.5, 'afternoon']
print(list1[-1:-5:-1]) # [20.5, 'afternoon', 'good', True]
print(list1[-1:-6:-1]) # [20.5, 'afternoon', 'good', True, 10]
print(list1[-1::-1]) # [20.5, 'afternoon', 'good', True, 10]
print(list1[::-1])
print(list1)
 
























