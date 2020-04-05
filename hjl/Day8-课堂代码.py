#字符串格式化符号
#1.%s
# name=input('请输入一个名字:')
# age=18
# add='北科'
# s1='我叫%s,我今年%s岁了,我现在在北京%s'% (name,age,add)
# print(s1)
#2.%d
# name=input('请输入一个名字:')
# age=18.5
# add='北科'
# s1='我叫%s,我今年%d岁了,我现在在北京%s'% (name,age,add)
# print(s1)

#2.%f
# name=input('请输入一个名字:')
# age=18.454646556
# add='北科'
# s1='我叫%s,我今年%.5f岁了,我现在在北京%s'% (name,age,add)
# print(s1)

#4.%e
# name=input('请输入一个名字:')
# age=18.45464655622222
# add='北科'
# s1='我叫%s,我今年%e岁了,我现在在北京%s'% (name,age,add)
# print(s1)

#5.%g
# name=input('请输入一个名字:')
# age=18.4546465563333
# add='北科'
# s1='我叫%s,我今年%e岁了,我现在在北京%s'% (name,age,add)
# print(s1)

#6.%o
# name=input('请输入一个名字:')
# age=18
# add='北科'
# s1='我叫%s,我今年%#o岁了,我现在在北京%s'% (name,age,add)
# print(s1)

#7.%x
# name=input('请输入一个名字:')
# # age=18
# # add='北科'
# # s1='我叫%s,我今年%#x岁了,我现在在北京%s'% (name,age,add)
# # print(s1)

#8.%c
# name=input('请输入一个名字:')
# age=97
# add='北科'
# s1='我叫%s,我今年%c岁了,我现在在北京%s'% (name,age,add)
# print(s1)

#字符串相关操作符
# s1='123'
# s2='123'
# #+
# print(s1+s2)
# print(s1)
# print(s2)
# #*
# print(s1*10)
# #in/not in
# print('1' in s1)
# print('1' not in s1)
# #
# s3='abc'
# print(s1>s3)

#补充字符串格式化
# name='huang'
# age=18
# num=10
# print(f'我叫{name},我今年{age}了')
# num=10
# print(f'我叫{name:{num}}')
# #序列相关方法

#1.max()
# max(iterable)
# print(max([10,20,30]))
# print(max((10,20,3)))
# print(max(range(5)))
# print(max('abc123'))

#2.min()
# print(min(10,20,-10,0))
# print(min([10,20,-10,0]))
# print(min((10,20,-10,0)))
# print(min('abc,.123'))
# print(min(range(5)))

#3.sum()
# print(sum([10,20,30],40))
# print(sum((10,20,30)))
# print(sum(range(5),2))
# print(sum('123'))

#4.reversed()
# rst = reversed([1,2,10,7])
# rst = reversed((1,2,10,7))
# rst = reversed('abc')
# rst = reversed(range(10))
# print(list(rst))
# for i in rst:
#      print(i)

#5.sorted()
# print(sorted([10,2,3,5,10,7,-3]))
# print(sorted([-10,2,3,-5,10,7]))
# print(sorted(range(5)))
# print(sorted('abaga123'))

#6.zip()
# rst=zip([1,2,3],[4,5,6],[7,8,9])
# rst=zip([1,2,3],[4,5,6],[7,8])
# rst=zip([1,2,3],'123',[4,5])
# rst=zip([1,2,3],range(5),[4,5])
# print(list(rst))

#7.enumerate()
# rst = enumerate([10,20,30],11)
# print(list(rst))
# rst = enumerate(range(5),11)
# print(list(rst))
# rst = enumerate('123',11)
# print(list(rst))
# rst = enumerate(('123',),11)
# print(list(rst))