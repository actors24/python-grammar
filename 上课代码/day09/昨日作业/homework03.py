
#3.传入:"HelloMyWorld" 返回:"Hello my world"

'''
遍历 字符串 第二个字符
每个字符 判断 如果是大写，变成 空格 + 小写 replace
'''
# s1 = "HelloMyWorld"
# s2 = s1[1:]
# for i in s2:
#     if i.isupper():
#         s2 = s2.replace(i,' ' + i.lower())
#
# print(s1[0] + s2) # Hello my world

s1 = "HelloMyWorld"
for i in range(1,len(s1)):
    print(i)
    if s1[i].isupper():
        s1 = s1.replace(s1[i],' ' + s1[i].lower())
print(s1) # Hello my world
