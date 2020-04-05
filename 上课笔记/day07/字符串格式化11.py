
name = '肖枫'
age = 3
hometown = '山东'
school = '蓝翔'
major = '挖掘机'

# 占位符
s1 = '我叫{0},我今年{1}岁，我来自{3},我毕业学校是{3}，专业是{3}。'
print(s1.format(name,age,hometown,school,major))

# 自我介绍
# print('我叫' + name + ',我今年' + str(age) + '岁，我来自' + hometown + ',我毕业学校是' + school + '，专业是' + major +'。')
# 变量拼接
# +
# a = 'abc'
# b = '123'
# print( a + b)  #123abc

# print('123' + 10)

# 最基本使用方式一: 数据要一一对应。顺序要一致，数量也要一致
# s2 = '我叫{},我今年{}岁了。 '
# print(s2.format('德兴',2))

# 方式二：{0} 可以使用 下标。 下标 一定要与 format中传入的数据 下标 对应范围内。不能超范围
s2 = '我叫{1},我今年{1}岁了。 '
print(s2.format('德兴',2))


# 方式三：{a} 可以使用变量名称 .format()传入数据时，需要使用 变量=值 变量赋值 形式 去传递
s2 = '我叫{b},我今年{a}岁了。 '
print(s2.format(a='德兴',b=2))
print(s2.format(b=2,a='德兴'))