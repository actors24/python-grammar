
'''
python3.6 字符串格式化

'''
name  = '郭继广'
age = 18
addr = '张家口'
print(f'我叫{name},我今年{age}了。来自{addr}')

# 通过 设置 当前字符串 长度  m.n
num = 10
print(f"我叫{name:{num}}。")