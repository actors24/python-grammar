# Python 语法基础

* 输出函数

~~~markdown
1. print(参数)
		将传入的参数，打印到控制台
		print(*value,sep='',end='\n',file=sys.stdout,flush=False)
		*value：要打印的内容，*表示可以传入多个参数（value对应的参数，可以是任何类型的数据）
		sep:如果打印多个数据，多数据要用sep这个字符串，进行分隔，sep默认是空格
		end：打印结束后，使用end这个字符串，作为结尾，默认是：\n 表示换行
		file：文件流
		flush：是否清空缓存		
~~~

~~~python
print(100)
print('abc')

print(1,2,3,4)
print()

print(100,200,300,sep='***')

print('C:\admin\hehe\notebook\abc')
# 文字注释，不参与编译
# \n： 在字符串中表示换行   转义字符

print(100,200,300,end='***')
print('hehe1')

print()

print('hehe2')
~~~

* 输入函数

~~~markdown
input
1. input()
		input(prompt=None)
		阻塞当前进程，等待用户在控制台输入数据，当输入回车按键，用户数据完毕，程序不再阻塞，继续执行，input会将用户输入的数据，返回到程序中
		如果prompt参数给出，则在用户输入之前，会打印一下prompt
		prompt：可以传入任何值
		input（）的返回值均为字符串
		
~~~

~~~python
# input('请输入一个整数：')
a=input('请输入一个字符串：')
print(a)
~~~

* 变量

~~~markdown
1. 变量内部存储的是 值的首地址
		任何一个包含其他数据首地址的内容，都称之为引用
		a=10  # a 存储了10的首地址  称：a是10的引用
2. 变量没有类型限制
		a=10
		a='abc'
		print(a) # 'abc' 
		变量中的内容，是动态变化的
3. 先赋值，后使用
4. 变量，如果重名，后出现的值，覆盖先出现的值
5. 要符合标识符命名规范
~~~

* 标识符命名规范

~~~markdown
任何和名字相关的内容，都叫做标识符
语法规范：
1. 合法标识符：字母，下划线，数字（数字不能开头）
2. 大小写敏感（区分大小写）
3. 不能使用保留字和关键字
		关键字：
			python内部使用的，不可更改的，不可赋值的，拥有特殊用法的内容
			if for while and or not is in else with True False def class break  continue  global nonlocal 
		保留字：
			python内部占用的名字，已经使用该名，实现了python使用的功能，可以更改的，可以赋值的内容
			不建议使用保留字作为变量，因为会修改保留字原有的功能，导致程序的异常
			print input sum help str list dict tuple float bool bytes set frozenst type isinstance 
4. 没有长度限制
		
开发习惯：
1. 望文生义
		变量名要尽量表现值的含义
2. 大小写：
		1. 包名，模块名：全小写
		2. 常量：全大写
		3. 类名：首字母大写，后面单词首字母也大写
				驼峰命名法
		4. 变量名，函数名，方法名：所有单词全小写，单词之间用下划线隔开（PEP8  python的书写风格规范）
~~~

* 数据类型

~~~markdown
1. python是没有类型的概念的
2. 如果一定要有类型：
		python中只有一个类型：对象类型
		10：整型对象
		‘abc’：字符串对象
		[1，2，3]：列表对象
		万物皆对象
3. 常见的数据对象类型：
		int：整型  integer
			 10  100
		float： 浮点型  float
			 1.5   100.0
			 科学计数法：
			 1.23e+10 
		bool： 布尔类型  boolean
			 True  False
		str： 字符串类型  string
			‘abc’  “abc”  '''abc''' """abc"""
			‘’：空串
		None:空值
		复杂类型：list，tuple,set,dict
		
4. 查看数据类型：
		type(数据)
		返回数据的类型
~~~

* 类型转换问题

~~~markdown
不同的数据相互转换类型
1. str--int   int()
2. str--float float()
3. int--str   str()
4. int--float float()
5. float--str str()
6. float--int int()

注意：
如果要将字符串，转换成整型或浮点型，保证字符串要兼容于数字
int（）是向0取整
~~~

---

* 表达式

~~~markdown
变量和字面值用某个式子连接的形式，称之为表达式
10--int   10是int的字面值
‘a’--str  ‘a’是str的字面值
~~~

* 运算符

~~~markdown
1. 一般运算符：
		+ - * /（真除法）  //（地板除法，向下取整）
        % （mod 模 本质上取余数） ** （幂运算）
2. 赋值运算符：
		=   ：  a=b   b赋值给a 
		增强赋值：
		+=
		-=
		*=
		/=
		//=
		%=
		**=
		
		a+=1   a=a+1
3. 布尔运算符：比较运算符
		==  ：是否相等
		！=  :是否不相等
		>=	:是否大于等于
		<=	：是否小于等于
		>	：是否大于
		<	：是否小于
		返回的所有值都是bool类型，True，False
4. 逻辑运算符：
		逻辑运算符前后可以有内容（not除外）
		and  :  a and b 
			a和b都为真，结果为真
			如果有任何一个为假，记过为假
        or 	：  a or b 
        	a或b只要有一个为真，结果就为真
        	如果两个都是假，结果才为假
        not	：  not a 
        	如果a为真，结果就是假
        	如果a为假，结果就是真
        bool值：
        	True：真 --- 1 
        	False：假--- 0
        	任何非零，都能代表True  
        		数字，非空数据等
        	任何零，都能代表False
        		0，[],'',None,{},()
        短路性：
        	如果逻辑运算中，第一个之，可以确定最终的真假结果，则逻辑运算符之后的数据，不再进行运算
        优先级： not>and>or
5. 三元运算符
		a=（值1 if 布尔运算 else 值2）
		如果布尔预算为真，返回值1
		如果布尔运算为假，返回值2
~~~

* 优先级

~~~markdown
1. 一般运算：
		先乘除，后加减
2. 元越少，优先级越高
		**： 一元运算符  
		+，-，*，/。。。 二元运算符
		三元运算符中三个元
		一元>二元>三元
~~~

---























