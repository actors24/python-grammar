# 1.a='''
# aaa
# bbb
# ccc
# '''
# a='aaa\nbbb\nccc'
#
# 2.用于定义多行字符串

# 3.print(s[12:18])

# 4.print(s[-15:-9])

# #1.
# str = "小明:87;小花:81;小红:97;小天:76;小张:74;小小:94;小西:90;小伍:76;小迪:64;小曼:76;张小四:33"
# sums=0
# b=0
# c=0
# str1=str.split(';')
# for i in str1:
#     a=i.split(':')
#     b=int(a[1])
#     sums+=b
#     c+=1
# d=sums/c
# print(d)
#
# #2.
# m=input('请输入一段字符串:')
# n=m.split(' ')
# # print(len(n))
# for i in range(len(n)//2+1):
#     n[i],n[len(n)-i-1]=n[len(n)-i-1],n[i]
#     a=' '.join(n)
# print(a)
#
# m=input('请输入一段字符串:')
# n=m.split(' ')
# n.reverse()
# v=str(n)
# print(v,type(v))
# #3.
m = input('请输入电话号码：')
if len(m) != 11 and m.isdigit() is True:
    print('号码必须为11位，请重新输入!')
elif m.startswith('1') is False and m.isdigit() is True:
    print('号码开头必须为1，请重新输入!')
elif m.isdigit() is False:
    print('号码必须全是数字，请重新输入!')
elif m.startswith('10') is True or m.startswith('11') is True or m.startswith('12') is True:
    print('号码头两位错误，请重新输入!')
else:
    print('此号码合法!')
