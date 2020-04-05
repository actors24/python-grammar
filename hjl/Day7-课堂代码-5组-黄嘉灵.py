# 元组遍历
# t=(1,2,3,4)
# for i in range(len(t)):
#     print(t[i])

# 元组相关操作符
# t1=(10,)
# t2=('jialing',12,True)
# +
# print(t1+t2)
# print(t1)
# print(t2)
#
# print(t1*3)
# print(t1)
# in not in
# print('jialing' in t2)
# print('jialing' not in t2)
# #比较运算符
# t3=(13,)
# print(t1>t3)

# 元组切片
# t1 = ('jialing',13,True,'male','haodi',22)
# # print(t1[1:5])
# # print(t1[1:])
# # print(t1[:])
# # print(t1[::2])
# # print(t1[::-1])
# # print(t1[-1:-5:-1])
# # print(t1[-5:-1])
# # print(t1)

# for-else
# for i in range(4):
#     print(i)
# else:
#     print('我是代码块')
#
# for i in range(4):
#     print(i)
#     if i==3:
#         print('当前i为3')
#         break
# else:
#     print('我是代码块')
#
# for i in range(100,201):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             print(i,'不是质数')
#             break
#         else:
#             print(i,'是质数')

# 字符串初识
# s1='123,.'
# print(s1,type(s1))
# s2='123,.\''
# print(s2,type((s2)))

# #字符串元素操作
# s1='1232ad.,.-嘉灵'
# #访问第一个元素
# print(s1[0])
# #字符串长度概念
# print(len(s1))
# print(s1[len(s1)-1])

# 字符串不能进行增删改操作

# 字符串遍历
# s1='abc123'
# for i in s1:
#     print(i)
# print(s1[:])
# print(s1[1:])
# print(s1[:5])
# print(s1[::-1])
# print(s1[-1:-4:-1])
# print(s1)
# print(type(s1))

# 字符串常用方法
# 1.count()
# s1 = 'sadf,.+---2fs'
# print(s1.count('a'))
# print(s1.count('0'))
# print(s1.count('a',1))
# print(s1.count('a',1,2))

# 2.find()
# s1 = 'sadf,.+---2fs'
# print(s1.find('0'))
# print(s1.find('1'))
# print(s1.find('a'))
# print(s1.find('a',1))
# print(s1.find('a',1,2))

# 3.capitalize()
# s1 = 'sadf,.+---2fs'
# print(s1.capitalize())
# print(s1)

# 4.casefold()
# s1 = 'sadf,.+---2fs'
# print(s1.casefold())
# print(s1)

# 5.lower()
# s1 = 'sadf,.+---2fs'
# print(s1.lower())
# print(s1)

# 6.upper()
# s1 = 'sadf,.+---2fs'
# print(s1.upper())
# print(s1)

# 7.isalpha()
# s1 = 'sadf,.+---2fs'
# print(s1.isalpha())
# print('123'.isalpha())
# print('abA'.isalpha())
# print(''.isalpha())
# print(' '.isalpha())
# print('德兴'.isalpha())
# print('ΑΒΓαβγδ'.isalpha())

# 8.isnumeric()
# print('123'.isnumeric())
# print('abc'.isnumeric())
# print('ΑΒΓαβγδ'.isnumeric())
# print('一'.isnumeric())
# print('二'.isnumeric())

# 9.isdigit()
# print('123'.isdigit())
# print('贰'.isdigit())
# print('二'.isdigit())
# print('Ⅱ'.isdigit())

# 10.islower()是否为全小写  isupper() 判断是否为全大写
# print('abc123'.islower())
# print('abc123'.isupper())

# 11.isspace()
# print(' abc'.isspace())
# print(' '.isspace())
# print('    '.isspace())

# 12.center()
# s1 = 'abc'
# rst = s1.center(11,'￥')
# print(rst)
# print(s1)
# for i in rst:
#     print(i)

# 13.ljust()
# print(s1.ljust(10,"￥"))
# print(s1)

# 14.rjust()
# print('aafaf'.rjust(12,'*'))

# 15.replace()
# s1 = 'abc123abc'
# print(s1.replace('a','*'))
# print(s1)
# print(s1.replace('a','*',-1))
# print(s1.replace('a','*',3))

# 16.split()
# s1 = 'abc#abc'
# print(s1.split('#'))
# print(s1.split('b'))
# print(s1.split(','))
# print(s1.split(' '))
# print(s1.split('a'))
# print(s1.split('b',1))

# 17.strip()
# s1 = ' a b c '
# print(s1.strip())
# print(s1)

# 18.endswith()
# print('endacd'.endswith('d'))
# print('endacd'.endswith('0'))
# print('endacd'.startswith('e'))
# print('endacd'.startswith('n',1))
# print('endacd'.endswith('c',0,5))

# 19.join()
# rst = '*'.join(['1','2','3'])
# # print(rst,type(rst))
# # rst = ' '.join('123')
# # print(rst,type(rst))

# 20.encode()
# rst='123'.encode()
# print(rst)
# print(rst.decode())

# 字符串分类
# s1='中国\n太美啦'
# s2='''
# aaa
# bbb
# ccc
# '''
# print(s1)
# print(s2)
# s3='中国'\
#     '太美啦'\
#     '好看'
# print(s3)

# 字符串格式化
# name='黄嘉灵'
# age='22'
# hometown='广东'
# school='中北'
# major='计算机'
# s1='我叫{},我今年{}岁，我来自{},我毕业院校是{},专业是{}'
# print(s1.format(name,age,hometown,school,major))
# s2='我叫{0},我今年{1}岁，我来自{2},我毕业学校是{3}，专业是{4}'
# print(s2.format(name,age,hometown,school,major))
# s3='我叫{a},我今年{b}岁，我来自{c},我毕业学校是{d}，专业是{e}'
# print(s3.format(a=name,b=age,c=hometown,d=school,e=major))
