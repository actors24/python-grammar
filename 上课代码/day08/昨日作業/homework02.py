
'''
2.将字符串按照单词逆序 (10分)
 输入一段字符串，已知字符串只由字母和空格构成，将字符串按照单词逆序
 传入"welcome to baizhi" 返回 "baizhi to welcome"

'''
'''
1.把原串 轉為 列表
2.列表 實現 倒序  
3.列表 轉為 字符串
'''

s1 = "welcome to baizhi"
# list1 = s1.split(' ')
# list1.reverse() # ['welcome', 'to', 'baizhi']
s1.split(' ').reverse()
# 切片
# print(list1[::-1]) # ['baizhi', 'to', 'welcome']
# print(list1) # ['baizhi', 'to', 'welcome']
# print(' '.join(list1)) #baizhi to welcome


# 列表 常用方法
# 元組 常用方法
# 字符串 常用方法