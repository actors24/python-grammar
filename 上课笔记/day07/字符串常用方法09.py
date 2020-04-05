
# 1.count()
# s1 = 'abac123efg,.+-'
# print(s1.count('a')) # 1
# print(s1.count('0')) # 0
# print(s1.count('a',1)) # 1
# print(s1.count('a',1,2)) # 0

# 2.find()
# s1 = 'abac123efg,.+-'
# print(s1.find('0'))  # -1
# print(s1.find('1'))  # 对应的下标
# print(s1.find('a'))  #  0
# print(s1.find('a',1))  #  2
# print(s1.find('a',1,2))  #  -1

# 3.capitalize()
# s1 = '1abAC123efg,.+-'
# print(s1.capitalize()) #Abac123efg,.+-
# print(s1) # abAC123efg,.+-

# 4.casefold()
# s1 = '1abAC123efg,.+-'
# print(s1.casefold()) # 1abac123efg,.+-
# print(s1) # 1abAC123efg,.+-

# 5.lower()
# IV 罗马数字  中文 一 二  壹 贰
# s1 = '1abAC123efg,.+-'
# print(s1.lower()) # 1abac123efg,.+-
# print(s1) # 1abAC123efg,.+-


# 6.upper()
# s1 = '1abAC123efg,.+-'
# print(s1.upper()) # 1ABAC123EFG,.+-
# print(s1) # 1abAC123efg,.+-

# 7.isalpha()
# ΑΒΓαβγδ  alphabetic 字母的
# s1 = '1abAC123efg,.+-'
# print(s1.isalpha()) # False
# print('123'.isalpha()) # False
# print('abA'.isalpha()) # True
# print(''.isalpha()) # False
# print(' '.isalpha()) # False
# print('德兴'.isalpha()) # True
# print('ΑΒΓαβγδ'.isalpha()) # True

# 8.isnumeric()  number数字
# print('123'.isnumeric())  # True
# print('abc'.isnumeric())  # True
# print('ΑΒΓαβγδ'.isnumeric())  # True
# print('贰'.isnumeric())  # True
# print('二'.isnumeric())  # True

# 9.isdigit()
# print('123'.isdigit())
# print('贰'.isdigit())
# print('二'.isdigit())
# print('II'.isdigit())

# 10.islower()是否为全小写  isupper() 判断是否为全大写
# print('abc123'.islower())  # True
# print('abc123'.isupper())  # False

#11.isspace()
# print(' abc'.isspace()) # False
# print(' '.isspace()) # True
# print('    '.isspace()) # True


# 12.center()
# s1 = 'abc'
# rst = s1.center(11,'*')
# print(rst) # ***abc****  ****abc****
# print(s1)
# # for i in rst:
# #     print(i)
#
# # 13.ljust()  left
# print(s1.ljust(12,"*")) # abc*********
# print(s1)
#
#
# # 14.rjust() right
# print(s1.rjust(12,'*'))  # *********abc\


# replace()
# s1 = 'abc123abc'
# print(s1.replace('a','*')) # *bc123*bc
# print(s1)
# print(s1.replace('a','*',-1)) # *bc123abc
# print(s1.replace('a','*',3)) # *bc123*bc

# split()
# s1 = 'abc#abc'
# print(s1.split('#'))  # ['abc', 'abc']
# print(s1.split('b'))  #['a', 'c#a', 'c']
# # print(s1.split(','))  #['abc#abc']
# # print(s1.split(' '))  #
# print(s1.split('a'))  # ['', 'bc#', 'bc']
# print(s1.split('b',1))  #['a', 'c#abc']  maxsplit

# s1 = '蒋浩楠:16,韩磊：60,鑫总:80,肖枫:3'   #统计几位同学平均年龄
# 获取每个年龄 求和 除以 人数
# 获取到每个年龄?
# print(s1.split(',')) # ['蒋浩楠:16', '韩磊：60', '鑫总:80', '肖枫:3']
# 方案一：再次分隔？
# 方案二：


#strip()
# s1 = ' a b c '
# print(s1.strip())
# print(s1)


# endswith()
# print('endacd'.endswith('d'))  # True
# print('endacd'.endswith('0'))  # False
# print('endacd'.startswith('e'))  # True
# print('endacd'.startswith('n',1))  #True
# print('endacd'.endswith('c',0,5))  #True


# join()  split()
# rst = '*'.join(['1','2','3'])
# rst = 'abc'.join(['1','2','3'])
# print(rst,type(rst))  # 1*2*3   str  1abc2abc3
# # rst = 'abc'.join(['abc','123',['123','456']])
# rst = 'abc'.join(('abc','123'))
# # rst = 'abc'.join(range(5))
# rst = 'abc'.join('123')
# rst = ' '.join('123')
# print(rst,type(rst))


# encode()  bytes 二进制字符串
rst = '123'.encode()
print(rst)  #b'123'
# 普通字符串 调用常用方法
print(rst.decode()) # 123
