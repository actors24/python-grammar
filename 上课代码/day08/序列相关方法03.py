
#1.max()
# # max(iterable)
# print(max([10,20,30])) #30
# # print(max([10,20,30,-10,'abc'])) #30
# print(max((10,20,3))) # 20
# print(max(range(5))) # 4
# print(max('abc123')) # c
#
# # max()
# # 输入 自己年龄，比较最大年龄
# # input()
# a = 10
# b = 20
#
# print(max(a,b)) # 40

# 2.
# print(min(10,20,-10,0)) # -10
# print(min([10,20,-10,0])) # -10
# print(min((10,20,-10,0))) # -10
# print(min('abc,.123')) # ,
# print(min(range(5))) # 0


# 3.
# print(sum([10,20,30],40)) # 100
# print(sum((10,20,30))) #
# print(sum(range(5))) #
# # print(sum('123',start=0)) #


# 4.reversed()  reversed class 类
# reverse() 列表常用方法 列表.reverse()
# 返回值：reverseiterator object  可迭代对象
# rst = reversed([10,20,10,7])
# rst = reversed((10,20,10,7))
# rst = reversed('123')
# rst = reversed(range(5))
# print(list(rst)) # [7, 10, 20, 10]
# # for i in rst:
# #     print(i)


# 5.sorted()
# # sort() 列表常用方法
# # abs()
# print(sorted([10,2,3,5,10,7,-3],key=abs)) #[2, 3, -3, 5, 7, 10, 10]
# print(sorted((10,2,3,5,10,7))) #[2, 3, 5, 7, 10, 10]
# print(sorted(range(5))) #[0, 1, 2, 3, 4]
# print(sorted('abaga123')) #['1', '2', '3', 'a', 'a', 'a', 'b', 'g']


# 6.zip()
# 返回值：zip object
# rst = zip([10,20,30],[40,50,60],[70,80])
# rst = zip([10,20,30],(40,50,60),[70,80])
# rst = zip([10,20,30],'123',[70,80])
# rst = zip([10,20,30],range(3),[70,80])
# print(list(rst)) # [(10,), (20,), (30,)]   [(10, 40), (20, 50), (30, 60)]


# 7.enumerate() 枚举
rst = enumerate([10,20,30],11)
print(list(rst)) # [(11, 10), (12, 20), (13, 30)]

rst = enumerate(range(5),11)
print(list(rst)) # [(11, 0), (12, 1), (13, 2), (14, 3), (15, 4)]

rst = enumerate('123',11)
print(list(rst)) # [(11, '1'), (12, '2'), (13, '3')]

rst = enumerate(('123',),11)
print(list(rst)) # [(11, '123')]

