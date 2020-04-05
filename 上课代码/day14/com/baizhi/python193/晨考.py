# class A:
#     age=18
#
#
# a=A()# a:变量  代表实例对象   A() 实例对象本身   A:类名   （）：创建，调用
#
# a.hehe=100  # hehe: 属性  --- 实例属性
#
# # 类属性： 和类相关的属性
# # 实例属性： 和实例对象相关的属性
#
# A.hehe=200  # hehe：类属性
#
# # . ：所属关系：    A.hehe:  想创建  A下的hehe属性
# #  a.hehe:  想创建a实例对象下的hehe
#
#
# class  B:
#     def abc(self):   # 无论是方法还是函数，调用才会执行
#         self.hehe=100   # 方法中的实力属性，只有执行了该行代码，才会生效（创建）、
#         print(self.hehe)
#
# b=B()
# b.abc() # 调用方法，方法中的代码会执行   hehe会被创建
# print(b.hehe)
#
# b.name='xiaobo'  # 变量=值   创建
# print(b.name)    # 变量     访问
#
# class E:
#     abc=100
#     def hehe(self):
#         # E.abc=100  # 创建类属性
#         print(E.abc)
#         print(self.abc) # 实例对象可以访问类属性
#
# # 实例属性：
# # 创建
# # 在类内部（方法内部）： self.属性名=值
# # 在类外部：实例对象.属性名=值
# # 访问：
# # 类内部：self.属性名
# # 类外部：实例对象.属性名
#
# # 类属性：
# # 创建：
# # 1. 类的内部，方法的外部： 属性名=值
# # 2. 方法内部：类名.属性名
# # 3. 类的外部：类名.属性名
# # 访问:
# # 1. 类的内部（方法内部）：self.类属性   或   类.类属性
# # 2. 类的外部： 实例对象.类属性  或 类.类属性
#
# # 混淆：
# class D:  # 类的属性是全类公有---所有人共用一份
#     age=18
#     def get_age(self):
#         self.age=20   # 创建实例属性  20
#         age=25        # 创建普通变量  age=25
#         print(self.age)  # self.age(优先访问实例属性)
#
# d=D()
# d.get_age()
# print(d.age) # age:实例属性
# # d：类属性age（公共的，不属于实例，但是可以借用）   实例属性age（属于当前实例自己的属性）
#
#
# class F:
#     age=18
#
# f=F()
# print(f.age)  # age:类属性（不是当前实例对象的，而是类借给实例对象的）
#
#
# # 实例对象.属性： 1. 可能是调用类属性   2. 可能调用实力属性
# # 类属性被调用方式： 1. 类名.属性名   2. 实例对象.属性名
#
# class G:
#     age=18
#     def get_age(self):
#         self.age=20
#
# g=G()
# print(g.age)  # g尚未创建实例属性age  调用的是类属性age
# g.get_age()  # self.age=20   创建了实例属性
# print(g.age)
# del g.age
# print(g.age)   # 类的属性是公有的，实例属性是各自拥有的，实例对象删除了自己的实例属性
# # del g.age
# # print(g.age)

# 类属性不受实例对象的影响    类属性可以影响实例对象


# self: 指代当前实例对象

class H:
    def hehe(self,age):  # hehe(self=h1,age=18)  self=h1: 把好h1的首地址，传递给了self
        self.age=age  # 创建实例属性  # self.age=age   h1.age=18

h1=H()  # 创建实例对象
h2=H()  # 创建实例对象
h3=H()  # 创建实例对象

h1.hehe(18)   # h1.hehe(18)---h1.hehe(h1,18)
print(h1.age)
h1.age=30  # 创建实例属性---   实例对象.属性=值


h2.hehe(20)
print(h2.age)

# 实例对象之间互不影响，相互独立

# 参数的传递的本质都是：首地址的传递

# 地址一样的对象，必定是同一个对象（内容必定相同）
# 地址不一样的对象，必定不同的对象（即便内容一样）

# 语言是龟叔写的，写语言不是靠思想，出现语言之前，并没有理论，所有的理论都是通过例子推导处来的
# 对象： 一切客观存在的事物
# 1. 类是对象的模板（例子：图纸-汽车）
# 2. 类是客观事务在人脑中的主观反应（小孩-动物园）
# 3. 类是对象共性的抽象（动物类--猫类+狗类+马类）  ** is a **

class A:
    def hehe(self):  # self 自动传递，传递当前实例对象
        print('hehe')
















































































