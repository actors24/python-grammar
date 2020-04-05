#10
# 1. 方法名和类属性同名
    # 后者覆盖前者
# 2. 方法名和实例属性同名
    # 实例属性遮蔽方法名  （本质：方法本质就是类属性）


# #
# class A:
#     def hehe(self):
#         print('this is a')
#
# class B(A):
#     def hehe(self):
#         print('this is b')
#
# b=B()
# b.hehe()
# a=A()
# a.hehe()


# 12
# class Bird:
#     def fly(self):
#         print('bird can fly')
#
# class QQ(Bird):
#     def fly(self):
#         print('QQ can\'t fly')
#
# qq=QQ()
# qq.fly()

#
# a=10 # a=int(10)
# a=int(100)  # int: class

# class A:  # 代码的缔造者
#     def __init__(self,name,age,sex):  # 在创建实例对象时自动调用
#         print('this is A')
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def hehe(self):
#         print('hehe')
#
#
# a=A('xiaobo',18,True)   # 代码的使用者
# print(a.name,a.age,a.sex)

# 受众群体： 类 --- 代码封装到一起了 --- 工具
# 代码： 类之外的代码，程序员要写的代码

# 1. 封装类的人： 只需要封装一次，以后每次都可以使用
# 2. 使用类的人： 每次需要类，则去调用，每次写的代码都不同


# class A(B):
#     def __init__(self):
#         super().__init__()  # super()--B()---父类对象


# #
# class A:
#     def __init__(self):
#         print('this is A')
#
# class B(A):
#     def __init__(self):
#         print('this is B')
#         super().__init__()
#
# class C(A):
#     def __init__(self):
#         print('this is C')
#         super().__init__()
#
# class D(B,A):
#     def __init__(self):
#         print('this is D')
#         super().__init__()
#
#
# D()

#
# # super()---mro()
# print(D.mro())
#
# # super()---mro()---调用mro继承链式关系中的下一个类
# # 一个类如果调用super() ---
#


# class A:
#     def __init__(self):
#         print('A')
#
# class B(A):
#     def __init__(self):
#         print('B')
#         super().hehe()  # super() --- 调用了mro关系中，当前类B 的下一个mro类--C
#         print('***')
# class C(A):
#     def __init__(self):
#         print('C')
#     def hehe(self):
#         print('我是C，不是A，我不是你爸爸，我是你兄弟')
#
# class D(B,C):
#     def __init__(self):
#         print('D')
#         super().__init__()
# D()
# print(D.mro())

# 24
# class Shape:
#     # 接口 --- 标准 --- 指导性意义
#     def area(self): # 面积
#         pass
#     def girth(self): #周长
#         pass
#
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#
#     def area(self): # 面积
#         return self.r**2*3.14
#
#     def girth(self): #周长
#         return 2*3.14*self.r
#
# class Rect(Shape):
#     def __init__(self,l,w):
#         self.l=l
#         self.w=w
#
#     def area(self):  # 面积
#         return self.w*self.l
#
#     def girth(self):  # 周长
#         return 2*(self.w+self.l)
#
# class Square(Rect):
#     def __init__(self,a):
#         self.a=a
#         super().__init__(a,a)
#
#     # def area(self):  # 面积
#     #     return self.a**2
#     #
#     # def girth(self):  # 周长
#     #     return self.a*4
#
# s=Square(5)
# print(s.area())
# print(s.girth())

# 22

# # 缔造者
# class Role:
#     def __init__(self,name):  # __init__(self_M,name)
#         self.name=name  # self_M.name=name   Magicer().name=name
#     def attack(self):
#         pass
#
# class Magicer(Role):
#     def __init__(self,level,name):
#         super().__init__(name) # super().__init__(self_M,name)
#         self.name=name
#         if level>10 or level<1:
#             self.level=1
#         else:
#             self.level=level
#     def attack(self):
#         return self.level*5
#
# class Soldier(Role):
#     def __init__(self, hurt, name):
#         super().__init__(name)
#         self.hurt=hurt
#     def attack(self):
#         return self.hurt
#
# class Team:
#     def __init__(self):
#         self.team=[]  # 为了保存每个角色
#         # team中的每一个元素： 角色（战士，魔法师）
#
#     def add_member(self,*roles): # 传入一个角色，包含了展示，魔法师
#         if len(self.team)+len(roles)>6:
#             print('团队已满')
#         else:
#             self.team.extend(roles)
#
#     def attack_sum(self):
#         sums=0
#         for role in self.team:
#             sums+=role.attack()
#         return sums
#
#
# # 测试：使用者
# m=Magicer(10,'hehe')
# m.name='heheheh'
#
#
# # 让多个角色组队
# t=Team()
# # 想团队中添加角色
# t.add_member(Magicer(10,'xiaobo'),
#              Magicer(10,'jiangang'),
#              Magicer(5,'liuhao'),
#              Soldier(100,'feige'),
#              Soldier(100,'maoxinyu'),
#              Soldier(50,'hanbowen'))
#
# print(t.attack_sum())
# for role in t.team:
#     print(role.name)

# 27
# class Stack:
#     def __init__(self,iterable):
#         # iterable:是一个可迭代对象
#         self.__l=[]
#         self.__l.extend(iterable)
#
#     def is_empty(self):
#         if self.__l:
#             return False
#         return True
#
#     def push(self,value):
#         self.__l.append(value)
#
#     def pop(self):
#         return self.__l.pop()
#
#     def top(self):
#         return self.__l[-1]
#
#     def bottom(self):
#         return self.__l[0]
#
#     def show_all_item(self):
#         return self.__l
#
# a=Stack('alksjdlak')
# # s=list([1,2,3]) #
#
# print(a.show_all_item())
# for i in a:
#     print(i)







# # 23
# class Account: # 银行账户
#     def __init__(self,id,balance,password):
#         self.id=id
#         self.balance=balance
#         self.password=password
#     def set_password(self,newpass):
#         if len(newpass)==6:
#             self.password=newpass
#     def get_password(self):
#         return None
#
# class Savingaccount(Account): # 储蓄账户
#     def __init__(self,id,password,balance,interestRate):
#         super().__init__(id,balance,password)
#         self.interestRate=interestRate
#     def set_interest_rate(self,rate):
#         if 0.1>rate>0:
#             self.interestRate=rate
#
# class CreditAccount(Account):# 信用账户
#     def __init__(self,id,password,balance,creditLine):
#         super().__init__(id,balance,password)
#         self.creditLine=creditLine
#
# class Bank:
#     def __init__(self):
#         self.l=[]
#
#     def open_account(self,id,password,types,balance=0,interestRate=0.02,creditLine=-1000):
#         '''
#         :param id: 账户
#         :param password: 账户密码
#         :param type: 账户类型 0：A 1：SA 2：CA
#         :return:
#         '''
#
#         if types==0:
#             self.account=Account(id,balance,password)
#         elif types==1:
#             self.account=Savingaccount(id,password,balance,interestRate)
#         elif types==2:
#             self.account=CreditAccount(id,password,balance,creditLine)
#         self.l.append(self.account)
#         return self.account
#
#     def deposit(self,a,amount):
#         '''
#         :param a: 存入账号，id
#         :param amount: 存入金额
#         :return: 余额
#         '''
#         for i in self.l: # l: 列表,元素是每一个账户
#             if i.id==a:
#                 # 多种用户不同操作
#                 i.balance+=amount
#
#     def withdraw(self,a,amount):
#         for acc in self.l: # l: 列表,元素是每一个账户
#             if acc.id==a:
#                 # 多种用户不同操作
#                 if type(acc)==CreditAccount:
#                     # 可以透支
#                     if (acc.balance-amount)>=acc.creditLine:
#                         #允许透支
#                         acc.balance-=amount
#                     else:
#                         print('额度不足')
#                 else:
#                     if acc.balance<amount:
#                         # 不让取
#                         print('余额不足')
#                     else:
#                         acc.balance-=amount
#




# 29
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
# class Line:
#     def get_len(self,p1,p2):
#         return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
#
#
# l=Line()
# print(l.get_len(Point(0,0),Point(3,4)))


# 25
class Employee:
    def __init__(self,name,birth):
        self.birth=birth
        self.name=name
    def get_salary(self,month,salary):
        # 如果过生日，奖励100元
        if self.birth==month:
            return salary+100
        return salary

class SalariedEmployee(Employee):
    def __init__(self,salary,birth,name):
        super().__init__(name,birth)
        self.salary=salary
    def get_salary(self,month):
        # 如果过生日，奖励100元
        return super().get_salary(month,self.salary)

class HourlyEmployee(Employee):
    def __init__(self,hour,name,birth):
        super().__init__(name,birth)
        self.hour=hour
    def get_salary(self,month):
        # 如果过生日，奖励100元
        # 每小时10元
        if self.hour>160:
            salary=(self.hour-160)*15+160*10
            return super().get_salary(month,salary)
        else:
            salary=self.hour*10
            return super().get_salary(month,salary)

class SalesEmployee(Employee):
    def __init__(self,sales,rate,name,birth):
        super().__init__(name,birth)
        self.sales=sales
        self.rate=rate
    def get_salary(self,month,salary1=0):# salary1=固定工资
        # 如果过生日，奖励100元
        salary2=self.sales*self.rate
        return super().get_salary(month,salary1+salary2)

class BasePlusSalaesEmployee(SalesEmployee):
    def __init__(self,salary,sales,rate,name,birth):
        super().__init__(sales,rate,name,birth)
        self.salary = salary
    def get_salary(self,month):
        # 如果过生日，奖励100元
        return super().get_salary(month,self.salary)



se=SalariedEmployee(10000,4,'xiaobo') # 10100
he=HourlyEmployee(160,'liuhao',5)  # 1600
see=SalesEmployee(1000000,0.05,'jiangang',5) # 50000
bpse=BasePlusSalaesEmployee(2000,1000000,0.05,'maoxinyu',4) # 52100
l=[]
l.extend([se,he,see,bpse])
for i in l:
    print(i.get_salary(4))

































