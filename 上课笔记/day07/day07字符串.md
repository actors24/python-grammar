## day07-字符串

* 概念

~~~python
列表 元组 可以保存多个数据 可迭代对象-for
字符串
	- 引号括起来的 单引号 双引号 三引号
    	- 单引号： ''
        - 双引号： ""  嵌套使用/配合使用\
        	s2 = "123,.'"
			s2 = '123,.\''  # 123,.' 
        - 三引号： '''123'''  """123""" 多用于 文档注释
    - 由字符组成的串
    	字符：数字 字母(英文大小写)，标点符号，特殊符号。。。
字符串 特点：
	- 可迭代对象 for循环
    - 有下标 
    - 支持 切片
    - 不可修改 不可变
~~~

字符串元素操作

~~~python
1.访问 查
	- 字符串[index]
    
增加  删除 修改 均不能
结论： 类似元组，不可修改    
~~~

字符串长度

~~~python
len(s) - 监听字符串长度，字符串中字符的总个数
~~~

字符串遍历 循环

~~~python
for循环

for i in s1:
    print(i)
~~~

字符串切片

~~~python
s1 = 'abc123'
print(s1[:])  #abc123
print(s1[1:])  #bc123
print(s1[:5])  #abc12
print(s1[::-1])  #321cba
print(s1[-1:-4:-1])  #321
~~~

字符串常用方法

~~~python
1.S.count(sub,[start,[end]])
	- 功能： 统计 sub 出现的次数
    - 返回值： >= 0 整数
    - 参数
    	- sub：要统计的元素
        - start：开始位置（包含该位置）。可省略，默认为0
        - end： 结束位置（不包含该位置）。可省略，默认为末尾
 	demo：
    	s1 = 'abac123efg,.+-'
        print(s1.count('a')) # 1
        print(s1.count('0')) # 0
        print(s1.count('a',1)) # 1
        print(s1.count('a',1,2)) # 0
2.S.find(sub,[start,[end]])
	- 功能： 查找sub在字符串中第一次出现的对应的下标
    - 返回值： index -1
    	- 如果找到，则返回值为 对应index
        - 否则，返回值 -1
    - 参数：
    	- sub： 要查找的字符
        - start：开始位置（包含该位置）。可省略，默认为0
        - end： 结束位置（不包含该位置）。可省略，默认为末尾
    demo：
    	s1 = 'abac123efg,.+-'
        print(s1.find('0'))  # -1
        print(s1.find('1'))  # 对应的下标
        print(s1.find('a'))  #  0
        print(s1.find('a',1))  #  2
        print(s1.find('a',1,2))  #  -1
3.S.index(sub,[start,[end]])
	- 功能： 查找sub在字符串中第一次出现的对应的下标
    - 返回值： index
    	- 如果找到，则返回值为 对应index
        - 否则，报错 valueError
    - 参数：
    	- sub： 要查找的字符
        - start：开始位置（包含该位置）。可省略，默认为0
        - end： 结束位置（不包含该位置）。可省略，默认为末尾
4.S.capitalize()
	- 功能：实现 首字母大写
    - 返回值： 新的字符串
    - 原字符串 不变
    s1 = 'abAC123efg,.+-'
    print(s1.capitalize()) #Abac123efg,.+-
    print(s1) # abAC123efg,.+-
5.S.casefold()
	- 功能：字符全部转换为小写
    - 返回值：形成小写的新的字符串
    - 原字符串 不变
6.S.lower()
	- 功能：所有英文字符转为小写
    - 返回值：新的字符串
    - 原字符串 不变
    demo:
        s1 = '1abAC123efg,.+-'
        print(s1.lower()) # 1abac123efg,.+-
        print(s1) # 1abAC123efg,.+-
7.S.upper()
	- 功能：所有英文字符转为大写
    - 返回值：新的字符串
    - 原字符串 不变
    demo:
        s1 = '1abAC123efg,.+-'
        print(s1.upper()) # 1ABAC123EFG,.+-
        print(s1) # 1abAC123efg,.+-
8.S.isspace()
	- 判断是否全为空格
    - 返回值： True/False
9.S.islower()
	- 判断是否全部为小写
10.S.isupper()
	- 判断是否全为大写
11.S.isnumeric()	
	- 判断是否为 有记数标记的 字符
    	阿拉伯数字 中文字符 各国字符  罗马 希腊。。
        
12.S.isalpha()
	- 判断是否为 字母 各国字母
13.S.isdigit()
	- 判断是否为 纯数字
14.S.center(width,[fillchar])
	- 功能：实现S字符串在新生成长串中居中
    - 原字符串 不变
    - 参数：
    	- width：指定新串的长度
        - fillchar：可选 填充字符。默认为 空格
15.S.ljust(width,[fillchar])
	- 功能：实现S字符串在新生成长串中 左对齐
    - 原字符串 不变
    - 参数：
    	- width：指定新串的长度
        - fillchar：可选 填充字符。默认为 空格
16.S.rjust(width,[fillchar])
	- 功能：实现S字符串在新生成长串中 右对齐
    - 原字符串 不变
    - 参数：
    	- width：指定新串的长度
        - fillchar：可选 填充字符。默认为 空格
17.S.replace(old,new,[count])
	- 功能：用new 替换 old
    - 返回值：新的字符串
    - 原字符串不变
    - 参数
    	- old：原字符串中 某个字符
        - new： 新的 要去做替换
        - count：可选。默认全部替换
        	- 可以指定替换的个数。从左到右进行指定个数替换。
    demo：
    	s1 = 'abc123abc'
        print(s1.replace('a','*')) # *bc123*bc
        print(s1)
        print(s1.replace('a','*',-1)) # *bc123*bc
        print(s1.replace('a','*',3)) # *bc123*bc
	
18.S.split(sep,maxsplit)
	- 功能：分隔字符串 形成一个列表
    - 返回值： 列表
    - 原字符串不变
    - 参数
    	- sep: 分隔符
        - maxsplit：分隔次数。可选。默认不填为全部分隔
        	- 也可传参数，指定分隔次数
            
19.strip()
	- 功能：去除字符串的 前后 空格  不包含中间
    demo：
    s1 = ' a b c '
	print(s1.strip())
20.endswith(suffix,[start,[end]])
	- 功能：判断字符串是否以suffix 结束。
    - 返回值：bool
    - 参数
    	- suffix： 指定字符
        - start：起始位置 包含该位置。可选。默认为0
        - end：结束位置 不包含该位置。可选。默认为末尾
21.startswith(prefix,[start,[end]])
	
	- 功能：判断字符串是否以prefix 开始。
    - 返回值：bool
    - 参数
    	- prefix： 指定字符
        - start：起始位置 包含该位置。可选。默认为0
        - end：结束位置 不包含该位置。可选。默认为末尾
22. S.join(iterable)
	- 功能：把可迭代对象中 元素(字符串类型) 拼接成 新字符串
    - 返回值： 新字符串
    - 参数：
    	-iterable
        	- list tuple str 不能是range
            - 以上iteralbe中元素必须为字符串
     demo：
    	rst = '*'.join(['1','2','3'])
        rst = 'abc'.join(['1','2','3'])
        print(rst,type(rst))  # 1*2*3   str  1abc2abc3
        # rst = 'abc'.join(['abc','123',['123','456']])
        rst = 'abc'.join(('abc','123'))
        # rst = 'abc'.join(range(5))
        rst = 'abc'.join('123')
        rst = ' '.join('123')
        print(rst,type(rst))
23.S.encode(encoding='utf-8',errors='strict')
	- 功能：生成一个二进制字符串
		- decode() 解码 普通字符串
~~~

字符串分类

~~~python
1.普通字符串
	'acb123.,+-'
2.二进制字符串  8进制 16进制
	b'123'
3.转义字符
	- 构成： \+普通字符 通过\ 对 普通字符 进行转义，生成特殊功能
	'abc\nabc'
    - \n 换行
    - \t 制表符
    - \" 转义" 失去原来意义 
    - \'
    - \\ \转义 \ 成为普通字符
4.原始字符串
	r'abc\n'
    
实现字符串  两行
肖峰
太帅啦
s1 = '肖峰\n太帅啦'
s2 = """
	肖峰
	太帅啦
"""
~~~

字符串格式化

~~~python
format()

最基本使用方式一: 数据要一一对应。顺序要一致，数量也要一致
# s2 = '我叫{},我今年{}岁了。 '
# print(s2.format('德兴',2))

方式二：{0} 可以使用 下标。 下标 一定要与 format中传入的数据 下标 对应范围内。不能超范围
s2 = '我叫{1},我今年{1}岁了。 '
print(s2.format('德兴',2))


方式三：{a} 可以使用变量名称 .format()传入数据时，需要使用 变量=值 变量赋值 形式 去传递
s2 = '我叫{b},我今年{a}岁了。 '
print(s2.format(a='德兴',b=2))
print(s2.format(b=2,a='德兴'))
~~~























































