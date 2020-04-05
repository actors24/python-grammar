 # 1.类是对象的模板,对象是类的实例

# 2.抽象，越笼统越抽象，越具体越具象

# 4.函数是直接写在文件中而不是class中, 方法只能写在class中;函数定义是def 函数名(), 函数里面的参数可写可不写, 而方法是定义在类中的, 而且方法必须带一个默认参数, 静态方法除外;函数的调用是直接写,方法的调用是通过对象点方法调用的

# 5.init()会被自动调用.

# 6.实例对象调用方法时,系统自动会把当前实例对象首地址传递,赋值给self,因为self指代的是当前实例对象;类调用方法时,此时需要手动传参给self,否则报错

# 7.
# class Person:
#     name = '黄嘉灵'
#     age = 18
#
#     def register(self):
#         print(self.name)
#
#
# a=Person()
# a.register()

# 8.
# class Worker:
#
#
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def work(self,time):
#         self.time = time
#         print(self.name,self.age,self.salary,time)
#
#
# a=Worker('jialing',22,20000)
# b=Worker('xiaofeng',21,10000)
# c=Worker('dengpeng',25,20000)
# a.work(8)
# b.work(10)
# c.work(12)

# 9.
# class Ticket:
#     price=100
#     weekend_price=120
#     children=50
#     weekend_children=60
#     def cal(self):
#         print(self.price*2+self.children)
#     def cal2(self):
#         print(self.weekend_price*2+self.weekend_children)
#
#
# Ticket().cal()
# Ticket().cal2()

# 10.
# class Address:
#
#     def __init__(self, address, zipcode):
#         self.address = address
#         self.zipcode = zipcode

# 11.
# class Address:
#
#     def __init__(self, address, zipcode):
#         self.address = address
#         self.zipcode = zipcode
#
#
# class Worker:
#
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def work(self, addr, zipcode):
#         self.addr = Address(addr, zipcode)
#         print(self.name, self.age, self.salary, self.addr.address, self.addr.zipcode)
#
#
# a = Worker('zhang3', 25, 2500)
# a.work('北京市海淀区清华园1号', 100084)

