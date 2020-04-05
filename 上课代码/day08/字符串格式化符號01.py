
# 1. %s

# name = input('请输入您的名字：')
# age = 18
# addr = '北科'
# s1 = '我叫%s，我今年%s岁了，我现在在北京%s' % (name,age,addr)
# print(s1)  # 我叫肖枫

# %s   str()
# name = '文韬'
# age = 18
# addr = '北科'
# # s1 = '我叫%s，我今年%s岁了，我现在在北京%s' % (name,age,addr)
# s1 = '我叫%s，我今年%#x岁了，我现在在北京%s' % ([10,20,30],255,addr)
# print(s1)  # 我叫肖枫

# print('%c' % 65)  # a
# center(width) ljust() rjust() 对齐方式 居中 左对齐 右对齐
print('%-20.8f' % 123.1234567891234)