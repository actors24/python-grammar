# 1.
# m=input('请输入一个字符串:')
# a=''
# b=''
# c=''
# d=''
# n=0
# for i in m:
#     if i.islower():
#         a=i.upper()
#         d=d+a
#     elif i.isupper():
#         b=i.lower()
#         d=d+b
#     else:
#         c=i
#         d=d+c
# print(d)

# 2.
# m=input('请输入一个字符串：')
# n=input('请输入你要查找的字符串：')
# print('字串出现的次数为：',m.count(n))

# 3.
# m=input('请输入一个字符串:')
# a=' '
# b=m[0]
# for i in range(1,len(m)):
#     if m[i].isupper():
#          b+=' '
#          b+=m[i]
#     else:
#         b+=m[i]
# c=b.split(' ')
# for j in range(1,len(c)):
#     c[j]=c[j].lower()
# d=' '.join(c)
# print(d)
