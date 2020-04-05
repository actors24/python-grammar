# 课堂代码
# 列表创建
# list1=[12,13.5,'hehe','阿富汗',True,False,None]
# print(list1)
# print(type(list1))

# list1=list()
# print(list1)
# print(type(list1))

# list1=[]
# print(list1)
# print(type(list1))

# a='hehe'
# list1=list(a)
# print(list1)1
# print(type(list1))4

# list1=list(range(10))
# print(list1)
# print(type(list1))
# print(list1[3])
# print(len(list1))
# print(list1[len(list1)-1])

# 列表元素操作
# list1=[12,13.5,'hehe','阿富汗',True,False,None]
# list1[1] = True
# print(list1)
# del list1[0]
# print(list1)
# list1[5] = 32
# print(list1[2])
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[5])
# for i in range(0,len(list1)):
#     print(list1[i])
# for i in list1:
#     print(i)
# 切片
# list1=[12,13.5,'hehe','阿富汗',True,False,None]
# print(list1[0:5])
# print(list1[:5])
# print(list1[1:6])
# print(list1[1:])
# print(list1[:])
# print(list1[0:5:2])
# print(list1[0:5:-1])
# print(list1[5:0:-1])
# print(list1[5:-1:-1])
# print(list1[::-1])
# print(list1[0:3])
# print(list1[2:2])
# print(list1[-5:-1:1])
# print(list1[-2:-5:-1])
# print(list1[-2:-5:-1])
# print(list1[-2:-7:-1])
# print(list1[-2::-1])
# print(list1[::-1])
# print(list1)

# 列表常用方法
# 1.append()
# list1 = [1,2,3]
# a = list1.append(4)
# print(list1)
# print(a)
# list1.append('5')
# print(list1)
# list1.append([True,False,None])
# print(list1)

# 2.extend()
# list1 = [1,2,3]
# a = list1.extend('4')
# a= list1.extend(range(1,10))
# a= list1.extend([4,5,6])
# print(list1)
# print(a)

# 3.insert()
# list1 = [1,2,3]
# a = list1.insert(1,4)
# a = list1.insert(-1,'12')
# a = list1.insert(-2,[5,6])
# print(list1)
# print(a)

# 4.clear()
# list1 = [1,2,3]
# a = list1.clear()
# print(list1)
# print(a)

# 5.pop()
# list1 = [1,2,3,4,5]
# list1 = []
# a = list1.clear()
# print(a)
# print(list1)

# 6.remove()
# list1 = [1,2,3,4,5]
# a = list1.remove(4)
# print(list1)
# print(a)

# 7.copy()
# list1 = [1,2,3]
# a = list1.copy()
# print(list1)
# print(a)

# 8.count()
# list1 = [1,2,3,4,5,6,4,3,5,4,4]
# a= list1.count(4)
# print(a)
# print(list1)

# 9.index()
# list1 = [1,2,3,4,5,6,4,3,5,4,4]
# a= list1.index(4,2,7)
# print(a)
# print(list1)

# 10.reverse()
# list1 = [1,2,3,4,5]
# a = list1.reverse()
# print(a)
# print(list1)

# 11.sort()
# list1 = [64,54.21,4,78]
# list1.sort(key=None,reverse=True)
# print(list1)

# 冒泡排序
# list1=[3,4,6,16,3,23,1,8]
# for i in range(8):
#     for j in range(8-i-1):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j+1]=list1[j+1],list1[j]
# print(list1)

# 选择排序
# list1=[3,4,6,16,3,23,1,8]
# for i in range(8):
#     for j in range(i+1,8):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)

# 课后作业
# 1.append(),extend(),insert()
# 2.append()是默认向列表末尾添加一个元素，extend()是默认向列表末尾添加多个元素
# 3.insert(1,'E')
# 4.[2,9,7]
# 5.[9,7]
# 6.不一样，因为第一个输出的是一个元素，第二个输出的是一个列表
# 7.a=[1,2,3]
#   a.insert(0,a[len(a)-1])
#   a.pop()
# 8.第一个表示原来的列表复制到另一个列表，对象是一样的，第二个表示产生一个新的列表，产生了不同的对象
# 9.list1[6][0]='wang5'
# 10.list1.sort(reverse=True)
# # 11.
# # 初始化列表
# a = [8, 6, 1, 3, 4, 2, 7, 5]
# # 求列表的长度
# # 外层循环控制轮数
# for i in range(len(a)):
#     # 每一轮要比较的元素的个数
#     for j in range(1, len(a) - i):
#         # 如果前一个数大于后一个数的话交换两个元素
#         if a[j - 1] > a[j]:
#             a[j - 1], a[j] = a[j], a[j - 1]
# # 打印排序好列表
# print(a)
# 12.
# # 初始化列表
# a = [1, 8, 4, 3, 6, 2, 7, 5]
# # 求列表的长度
# # 外层循环控制轮数
# for i in range(len(a) - 1):
#     # 每一轮要与i比较的元素的个数
#     for j in range(i + 1, len(a)):
#         # 如果a[i]大于a[j]的话，交换两个元素
#         if a[i] > a[j]:
#             a[i], a[j] = a[j], a[i]
# # 打印排好序的列表
# print(a)
# 13.
# n = int(input('请输入一个整数:\n'))
# # 让判断的数从2到n-1
# for i in range(2, n):
#     # 初始化一个拥有i个元素，每个元素均为True的列表
#     a = [True] * i
#     # j作为i的因子从2开始到i-1作为除数
#     for j in range(2, i):
#         # 如果i能被j整除，a[j]当中的元素改为False
#         if i % j == 0:
#             a[j] = False
#     # 如果False不在a列表的话说明i是质数
#     if False not in a:
#         # 打印所有质数
#         print(i, end=' ')
# print()
# 14.
# # 初始化一个元素从1-15的列表
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# # 设置一个循环，让报数一直进行下去，直到条件满足跳出
# while 1:
#     # 每次报六个人安全
#     for i in range(6):
#         # 向列表末尾添加列表的第一个元素
#         a.append(a[0])
#         # 列表的第一个元素删除
#         del a[0]
#         # 如果前六个数操作完删除第七个报数的人
#         if i == 5:
#             del a[0]
#     # 如果最后剩余1个人的话，游戏结束，跳出循环，打印赢家
#     if len(a) == 1:
#         print('猴子大王是:', a[0], '号')
#         break
