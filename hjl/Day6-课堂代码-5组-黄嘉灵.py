# #二维列表访问
# l1=[1,2,[3,4]]
# #访问内部列表中第一个元素
# l1[2]
# print(l1[2])
# l2=l1[2]
# print(l2[0])
#
# l1=[1,2,[3,4]]
# for i in l1:
#     if isinstance(i,list)==True:
#         for j in i:
#             print(j)
#     else:
#         print(i)

# #列表操作符
# l1=[1,2,3]
# l2=[4,5,6]
# print(l1+l2)
# print(l1)
# print(l2)
# print(l1+[7])
# print(l1*3)
# print(3 in [1,2,3])
# print(3 not in [1,2,3])
#
# #比较运算符
# l1=[1,2,3]
# l2=[4,5,6]
# print(l1>l2)
# l3=[12,'adda',True]
# l4=['sdf',23,False]
# print(l3<l4)
# l3=[10,11]
# l4=[3.4,11]
# print(l3>l4)
# #字符串比较每个字符ASCII值
# l3=['ab','ec','de']
# l4=['we','ff','ed']
# print(l3>l4 and l3<l4)

# #元组创建
# t1=(1,2,True,'aad')
# print(t1)
# print(type(t1))
#
# t1=('12,.3',True)
# print(t1)
# print(type(t1))
#
# t1=1,2,3
# t1=1,
# print(t1)
# print(type(t1))
#
# tuple()
# print(tuple())
#
# #可迭代对象 str list raange ttuple
# t1=tuple('huangjialing')
# print(t1)
# t1=tuple(['jialing','NO.1'])
# print(t1)
# t1=tuple(range(5))
# print(t1)
# t1=tuple((1,2,3))
# print(t1)

# #元组元素操作
# t1=(1,2,3)
# print(t1[1])
# t1[1]=4
# del t1[1]
# t1[2]='kfnsksdk'

# #元组常用方法
# t1=(1,2,3,4,2,3,2,)
# print(t1.count(2))
# print(t1.index(4,0,4))
