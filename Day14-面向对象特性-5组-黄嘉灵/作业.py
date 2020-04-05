# 3.一个类的属性是另一个对象，称这种配合的形式为组合

# 4.子类可以继承父类的成员，但是不能继承私有成员；如果子类没有初始化方法，则会调用父类的初始化方法；如果子类和父类都没有初始化方法，则会调用object的初始化方法；如果子类实现了和父类同样的方法，子类的方法会遮蔽父类的方法；python是多继承的，可以继承多个父类

# 5.继承和组合是两个不同的概念，继承是类和类之间的关系，而组合是一个类中的属性是另一个对象

# 10.方法名和类属性同名，后者覆盖前者；放发名和实例属性同名，实例属性遮蔽方法名

# 11.不会，子类的属性或方法会遮蔽父类的属性或方法，不会删除父类的属性或方法。

# 12.企鹅类也定义一个同鸟类飞的同名方法，这样就可以遮蔽父类的飞的方法

# 13. super()用于调用下一个父类并返回父类实例的方法; super(type)-> 未绑定的super对象;super(type,obj)->绑定super对象，需要isinstance(obj,type);
# super(type,type2)->绑定super对象，需要isinstance(type2,type)

# 15.num和count为类属性,x和y为实例属性

# 16.printBB方法中没有写默认参数self,self是必须要有的，他代表当前实例对象

# 17.A类被重复调用，浪费空间，造成资源浪费

# 18.使用super().__init__()替代父类.__init__(),这样就能保证所有的继承关系相关的类只会出现一遍，避免了资源浪费。

# 22.


class Role:
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass


class Magicer(Role):
    hurt = 5

    def __init__(self, name, level):
        super().__init__(name)
        if level > 10 or level < 1:
            self.level = 1
        else:
            self.level = level

    def attack(self):
        return self.level * self.hurt


class Soldier(Role):
    def __init__(self, name, hurt):
        self.hurt = hurt
        super().__init__(name)

    def attack(self):
        return self.hurt


class Team:
    def __init__(self):
        self.l = []

    def add_member(self, *member):
        if len(self.l) + len(member) > 6:
            print('本队已满')
        else:
            self.l.extend(member)
            print('添加成功')

    def attack_sum(self):
        self.sum = 0
        for i in self.l:
            print(i.name, i.attack())
            self.sum += i.attack()
        return self.sum


a = Magicer('jialing', 6)
b = Magicer('xiaofeng', 8)
c = Magicer('dengpeng', 10)
d = Soldier('yangkun', 200)
e = Soldier('sadda', 400)
f = Soldier('sfdf', 300)
t1 = Team()
t1.add_member(a, b, c, d, e, f)
# for i in t1.l:
#     print(i.name)
print(t1.attack_sum())


#
# 23.
# class Account:
#     def __init__(self,id,balance,pwd):
#         self.__id=id
#         self.__balance=balance
#         self.__pwd=pwd
#     def set_pwd(self,pwd):
#         if len(str(pwd))==6:
#             self.__pwd=pwd
#         else:
#             print('密码格式错误')
#
#     def get_pwd(self):
#         return None
#
#
# class CreditAccount(Account):
#     def __init__(self,id,balance,pwd,creditLine):
#         super().__init__(id,balance,pwd)
#         self.__creditLine=creditLine
#
#     def get_creditLine(self):
#         return self.__creditLine
#
#     def set_creditLine(self,creditLine):
#         self.__creditLine=creditLine
#
#
# class SavingAccount(Account):
#     def __init__(self,id,balance,pwd,interestRate):
#         super().__init__(id,balance,pwd)
#         self.__interestRate=interestRate
#     def get_interestRate(self):
#         return self.__interestRate
#     def set_interestRate(self,interestRate):
#         if 0<interestRate<0.1:
#             self.__interestRate=interestRate
#         else:
#             print('利率格式不对')
#
# a=CreditAccount('1100',100,123456,10000)
# print(a.get_creditLine())
# a.set_creditLine(20000)
# print(a.get_creditLine())
#
# b=SavingAccount('1101',1000,123456,0.05)
# print(b.get_interestRate())

# 24.
# class Shape:
#     def area(self):
#         pass
#
#     def girth(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self, banjin):
#         self.banjin = banjin
#
#     def area(self):
#         print(f'园的面积为{self.banjin ** 2 * 3.14}')
#
#     def girth(self):
#         print(f'圆的周长为{self.banjin * 2 * 3.14}')
#
#
# class Rect(Shape):
#     def __init__(self, long, width):
#         self.long = long
#         self.width = width
#
#     def area(self):
#         print(f'矩形的的面积为{self.long * self.width}')
#
#     def girth(self):
#         print(f'矩形的周长为{(self.long + self.width) * 2}')
#
#
# #
# #
# class Square(Rect):
#     def __init__(self, long):
#         self.long = long
#
#     def area(self):
#         print(f'正方形的的面积为{self.long ** 2}')
#
#     def girth(self):
#         print(f'正方形的周长为{self.long * 4}')


# c = Circle(2)
# c.area()
# c.girth()
# r = Rect(3, 4)
# r.area()
# r.girth()
# s = Square(3)
# s.area()
# s.girth()

# 25.
class Employee:
    def __init__(self, name, birth_month):
        self.__name = name
        self.__birth_month = birth_month

    def getSalary(self, month):
        if self.__birth_month == month:
            return 100
        else:
            return 0


class SalariedEmpolyee(Employee):
    def __init__(self, name, birth_month, salary):
        super().__init__(name, birth_month)
        self.__salary = salary

    def getSalary(self, month):
        return self.__salary + super().getSalary(month)


class HourlyEmployee(Employee):
    def __init__(self, name, birth_month, hours, hourlys):
        super().__init__(name, birth_month)
        self.__hours = hours
        self.__hourslys = hourlys

    def getSalary(self, month):
        if self.__hours > 160:
            self.__salary = 160 * self.__hourslys + (self.__hours - 160) * (self.__hourslys * 1.5) + super().getSalary(
                month)
        else:
            self.__salary = self.__hours * self.__hourslys + super().getSalary(month)
        return self.__salary


class SalesEmployee(Employee):
    def __init__(self, name, birth_month, sales, rate):
        super().__init__(name, birth_month)
        self.__sales = sales
        self.__rate = rate

    def getSalary(self, month):
        self.__salary = self.__sales * self.__rate + super().getSalary(month)
        return self.__salary


class BasePlusSalesEmployee(SalesEmployee):
    def __init__(self, name, birth_month, sales, rate, baseSalary):
        super().__init__(name, birth_month, sales, rate)
        self.__baseSalary = baseSalary

    def getSalary(self, month):
        self.__salary = self.__baseSalary + super().getSalary(month)
        return self.__salary


a = SalariedEmpolyee('jialing', 10, 10000)
print(a.getSalary(10))
b = SalesEmployee('xiaofeng', 10, 1000, 0.6)
print(b.getSalary(8))
c = HourlyEmployee('dengpeng', 10, 200, 30)
print(c.getSalary(8))
d = BasePlusSalesEmployee('zhaolin', 10, 200, 0.6, 3000)
print(d.getSalary(10))

# 26.
# l=[]
# l.append(a.getSalary(1))
# l.append(b.getSalary(2))
# l.append(c.getSalary(3))
# l.append(d.getSalary(4))
# for i in l:
#     print(i)

# 27.
# class Stack:
#     def __init__(self, *stack):
#         self.stack = []
#         self.stack.extend(stack)
#
#     def isEmpty(self):
#         if self.stack:
#             return False
#         return True
#
#     def push(self, obj):
#         self.stack.append(obj)
#
#     def pop(self):
#         if not self.stack:
#             print("当前栈为空")
#
#         else:
#             self.stack.pop()
#
#     def top(self):
#         if not self.stack:
#             print("当前栈为空")
#
#         else:
#             print(self.stack[-1])
#
#     def bottom(self):
#         if not self.stack:
#             print("当前栈为空")
#
#         else:
#             print(self.stack[0])
#
#     def clear(self):
#         self.stack.clear()
#
#     def show_all_item(self):
#         return self.stack
#
#
# a = Stack(1, 2, 3, 4, 5)
# a.clear()
# print(a.isEmpty())
# print(a.show_all_item())

# 28.
# class Account:
#     def __init__(self, id, balance, pwd):
#         self.__id = id
#         self.__balance = balance
#         self.__pwd = pwd
#
#     def set_pwd(self, pwd):
#         if len(str(pwd)) == 6:
#             self.__pwd = pwd
#         else:
#             print('密码格式错误')
#
#     def get_pwd(self):
#         return None
#
#
# class CreditAccount(Account):
#     def __init__(self, id, balance, pwd, creditLine):
#         super().__init__(id, balance, pwd)
#         self.__creditLine = creditLine
#
#     def get_creditLine(self):
#         return self.__creditLine
#
#     def set_creditLine(self, creditLine):
#         self.__creditLine = creditLine
#
#
# class SavingAccount(Account):
#     def __init__(self, id, balance, pwd, interestRate):
#         super().__init__(id, balance, pwd)
#         self.__interestRate = interestRate
#
#     def get_interestRate(self):
#         return self.__interestRate
#
#     def set_interestRate(self, interestRate):
#         if 0 < interestRate < 0.1:
#             self.__interestRate = interestRate
#         else:
#             print('利率格式不对')
#
#
# class Bank:
#     def __init__(self):
#         self.l=[]
#     def open_account(self, id,pwd, type):
#         if type == 0:
#             self.account = Account(id,0, pwd)
#         elif type == 1:
#             self.account = SavingAccount(id, 0, pwd, 0.08)
#         elif type == 2:
#             self.account = CreditAccount(id, 0, pwd, 10000)
#         else:
#             print('输入有误')
#         return self.account
#
#     def deposit(self, a, amount):
#         a.setBalance(amount + a.getBalance())
#         return a.getBalance()
#
#     def withdraw(self, a, amount):
#         if a.getBalance() < amount:
#             print('你的余额不足')
#         else:
#             a.setBalance(a.getBalance() - amount)
#             return a.getBalance()
#
#
# a = Bank()
# a.open_account('1100', 123456, 0)
# a.deposit('1100', 10000)

# 29.
# import math
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def getX(self):
#         return self.x
#
#     def getY(self):
#         return self.y
#
#
# class Line:
#     def __init__(self, p1, p2):
#         self.x = p1.getX() - p2.getX()
#         self.y = p1.getY() - p2.getY()
#
#         self.line = math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
#
#     def getLen(self):
#         return self.line
#
#
# p1 = Point(1, 2)
# p2 = Point(4, 6)
# line = Line(p1, p2)
# print(line.getLen())

# class A:
#     def __init__(self):
#         print('a')
#
# class B(A):
#     def __init__(self):
#         print('b')
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print('c')
#         super().__init__()
#
# class D(B,C):
#     def __init__(self):
#         super().__init__()
#         print('d')
#
#
# D()
# print(D.mro())
