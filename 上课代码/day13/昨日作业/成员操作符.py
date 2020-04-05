
# print('n' in 'Nn')
# print('N' in 'Nn')
# print('Nn' in 'Nn')


# 成员操作符
name = '193'

# 成员运算符 in not in 检测某个元素是否存在于 某个数据中
# 列表： 10 in [10,0,20]
# 元组： '123' in (10)
# 字符串： '123' in ‘12344’
# 字典： '123' in {‘ke':'va1',}

# 判断效率高？ 字典

dict1 = {'name':'193','age':2,'addr':'沙河'}

print(name in dict1)  # False
print(name not in dict1)  # True
print('age' in dict1)  # True
# print('name':'193' in dict1)  # True