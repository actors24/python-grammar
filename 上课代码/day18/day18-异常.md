## day18-异常

* 常见异常

~~~markdown
typeERROR 类型异常 +
nameerror 名字异常 
valueError 值异常 remove()
keyError 键异常
attributeError
indexError
SyntaxError语法异常
assertionerror 断言异常
osERROR 
filenotfoundError

~~~

* 异常处理

~~~markdown
异常 报错 不一定是坏事
实际开发过程中，尽量保证程序的健壮性，尽可能容错性更多。
~~~

* 异常处理方式

~~~markdown
1. try-except
	try:
		测试代码
	except 异常类型 (as 变量名)：
		异常处理代码块
	- try执行 测试代码，如果测试代码没有异常，则执行完毕之后，try-except结构结束
	- try执行 测试代码，一旦测试某一行出问题，则之后测试代码不会执行，直接进入到except结构进行异常捕获，如果异常类型匹配，则捕获成功，执行 异常处理代码块；否则except不能捕获成功，则由python异常机制来处理。
	- except 异常类型 as 变量名
		- 变量名：表示当前异常类型具体的错误提示参数/提示信息

2. try-多个except
	try:
		测试代码
	except 异常类型1 as tips1:
		异常类型1处理
	except 异常类型2 as tips2:
    	异常类型2处理
    except 异常类型3 as tips3:
    	异常类型3处理
    ...
   - 尝试执行测试代码，一旦测试代码出现问题，则会到多个except结构中进行逐一比对，如果某个except比对成功，则进入该 异常类型处理代码块；否则，python内置异常捕获机制启动处理
   - 注意：常见异常，实际上是一个一个类实现的。而常见类都是继承自Exception。Exception的父类是BaseException。所以在进行多个except结构书写时，需要注意前后顺序问题，尽量父类(范围广的异常)放在后面，从而避免直接放在前面拦截掉后面的异常类型。

	- 特殊写法：
		try:
			测试代码
		except:
			异常处理代码块
3. try-except-finally
	try:
		测试代码
	except 异常类型1 as tips1:
		异常类型1处理
	...
	finally:
		finally代码块
	- 尝试测试代码有问题，except结构成功捕获异常，仍会执行finally代码块
	- EXCEPT结构未能成功捕获，仍会执行
	- 测试代码无问题，也会执行
	- 不管测试代码有无问题，都会执行finally。
~~~

* 自定义异常

~~~markdown
实际开发中，python内置异常不能满足需要，则需要开发人员自己定义异常，称为 自定义异常
语法规范：
	- 必须遵循 异常 创建的 语法要求
	- 必须是一个 类，并且有继承关系存在。需要使用raise关键主动抛出异常
		常见异常的父类是 Exception，						Exception(BaseException)  					BaseException(object)
意义：
	- 自定义异常也会提高当前程序的容错性，尽可能实现开发人员程序开发时异常处理，而不会出现程序崩溃(终止)。
~~~

~~~markdown
class NoTicketError(Exception):
    def __init__(self, s):
        self.s = s
    def __str__(self):  # 类似 __init__() 方法 魔法方法-针对python
        print('我是__str__')
        return self.s
try:
    num = input('请输入数字')
    if int(num) == 10:  # 类型异常  False
        print('还有票，给你一张就行！')
    else:
        print('我想随便来个异常')
        raise NoTicketError('我是NoTicketError')

except NoTicketError as tips:
    print(tips) # 异常提示信息 异常参数 我是NoTicketError
    print('没有票啦！')
    
    
~~~

* 异常捕获特殊使用

~~~markdown
1. 文件操作 异常捕获
 try:
    with open('11.txt') as f:
        print(f.read())
except:
    print('文件不存在')
    - 结合使用try-except进行文件操作时异常处理，提高程序容错性
    - 使用 with 语句
    	- with：和 与 
    	- as 变量名： 变量名-开启的文件操作流
    		类似 f = open()
    	- 优势：如果文件操作正常执行，则执行完毕后不需要手动调用close(),而该结构会自动关闭操作流，释放资源。
2. try-except-else-finally
	语法：
		try：
			测试代码块
		except 异常类型：
			异常处理1
		except 异常类型：
			异常处理2
		。。。
		else:
			else代码块
		finally:
			finally代码块
	- 测试代码如果能够正常执行，没有异常，则会执行else代码块，并且其执行完毕之后，最后执行finally
	- 如果测试代码有异常，不管except结构是否能成功匹配，都不会执行else代码块，但都会执行finally
	
~~~

* for else

~~~markdown
for 变量 in 可迭代对象：
	循环体
else:
	else代码块
- 注意： 如果for循环能够正常执行完毕，则会执行else代码块
~~~

~~~markdown
for i in range(5):  # 0 1 2 3 4
    print(i)
    if i == 4:
        break
else:
    print('我是else代码块')
~~~

* while-else

~~~markdown
1. 语法规范
	while 布尔表达式：
		循环体
	else:
		else代码块
- 注意：
	同上 for else
~~~

~~~markdown
n = 0
while n < 5:
    print(n)    # 3
    n += 1
    if n == 4:
        break
else:
    print('我是else代码块')
~~~

* random模块

~~~markdown

~~~

