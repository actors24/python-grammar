## day16-模块

* 模块是什么？

~~~markdown
引言：
	for循环 代码块 相对完整 一段代码块
	if分支  代码块 
	函数 特定功能的代码块 
	面向对象 类 更高一级代码块 
模块： 本质上，就是一个个文件。文件内容：函数 类  
~~~

* 模块 分类

~~~python
引言：
	- 程序开发时，项目代码分解为一个个文件。低耦合  
    - 主模块 当前模块 构成程序中主文件。 main（）
    - 其他模块 其他文件 作为‘导入模块import’来使用。 类似 login() register() 
针对python，模块划分为三大类：
	- 内置模块  
    	- python内部设置好，python自带的   
    - 自定义模块 
    	- 自己构建的  
    - 第三方模块
    	- 别人写的 pypi网站  python package index 
        - 单独存放位置 在python安装目录中Lib下的site-packages 目录下
~~~

* 使用模块

~~~markdown
1. import 模块名
	- import 意思：导入
	- import functools  内置模块functools
	- 自定义模块
		- 内容： 尽量是完整的封装的代码块，比如 函数，类，全局变量。尽量不要有全局测试打印语句，如果必须要有，也可以间接实现。
~~~

* name

~~~markdown
if __name__ == '__main__':  # 主要的
    # 测试 打印语句
    print('我是module01的打印语句')
__name__: 可以用来监听，当前文件是否作为主程序来运行。
	- 如果作为主程序来运行，则 结果为 __main__
	- 如果不是作为主程序，(作为导入模块)，结果为 当前模块名字
注意：
	- 如果py文件中需要有一些专属于本身文件自己的测试性代码时，建议存放在 当前 if __name__ == '__main__'分支内部。
	则 只有在 该文件作为主程序运行时才会执行分支内部的代码。
~~~

* （正式）使用模块

~~~markdown
1.使用关键字 import
2.导入后，使用内容，语法规范： 点语法  模块名.属性
	- 模块名.全局变量
	- 模块名.函数()
	- 模块名.类()
3.模块名 尽量不要与当前文件中的全局变量/全局函数名/全局类名 同名，否则会出现 覆盖。
~~~

* 导入模块方式 （同级目录）

~~~markdown
1. import 模块名1,模块2,模块3.。。
	- 使用内容：模块名.属性
	- 可以一次性导入多个模块，逗号隔开即可
2. import 模块名 as  别名
	- 可以给当前导入模块名 起 别名.
	- 注意：别名 也不要 与 当前文件中的 命名 冲突，否则也会发生覆盖
	- 如果同时导入多个模块，分别起别名，则需要按下面规则：
		import 模块名1 as 别名1，模块名2 as 别名2，。。。。
		demo:
		import module03 as aa,a as aaa
注意：以上 导入方式，是针对于 同级目录下 可以直接使用import导入，或者是 内置模块 也可直接使用import导入
~~~

* 包

~~~markdown
管理文件的文件目录，类似 文件夹
	- 明显标志(区分于普通文件夹): __init__.py文件
包管理下的项目目录
	- dangdang
		- manage.py  
		- dangdang 子包
			- __init__.py
			- setttings.py
			- urls.py
			- wsgi.py
		- userapp 子包
			- migrations 子包
				- __init__.py
				- 0001_migrations.py 
			- __init__.py
			- views.py
			- urls.py
			- admin.py
			- models.py
~~~

* 包内模块导入

~~~markdown
1. from 包名.包名 import 模块名
	- 包名：不在同级目录中，所以如果有需要，从最顶级的包开始，逐级目录来导入，即 from 包名1.包名2.包名3 import 模块名,直到 所需模块所在的包，然后再来 import 即可
	- 如果从当前包中可能需要使用多个模块，则 
		from 包名 import 模块名1,模块名2，。。。
	- 如果要给模块名 起 别名，则
		from 包名 import 模块名1 as 别名1，模块名2 as 别名2，。。。

2. import 包名
	- 导入 该包内的 __init__.py模块
3. import 包名1.包名2.包名3.模块
	- 可以导入多个模块
	import 包名1.模块1，包名2.模块2，。。。。
4. import 包名1.模块1 as 别名
	- 可以同时导入多个模块
	import 包名1.模块1 as 别名1，包名2.模块2 as 别名2，。。。
~~~

* 总结

~~~markdown
__name__:
	if __name__ == '__main__': 
		print() 
模块导入 方式 
	- 同级目录下 import 模块 
	- 包 
		- import 包名.baoming.模块
		- from 包名 import 模块
		- 起别名
			from baoming import 模块 as 别名
			import 包名.模块 as 别名
模块分类：
	- 内置模块
	- 自定义模块
	- 第三方模块 site-packages目录
模块作用：
	- 复用性高 调用灵活
	- 实现 模块化开发，降低 代码耦合度，低耦合
	- 可维护性高 	
~~~

* 时间模块

~~~markdown
time模块
date模块
datetime模块

time内置模块
~~~

