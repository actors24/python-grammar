#22.
# class Role:
#     def __init__(self,name):
#         self.name=name
#
#     def attack(self):
#         pass
#
#
# class Magicer(Role):
#     def __init__(self,name,level):
#         super().__init__(name)
#         if level>10 or level<1:
#             self.level=1
#         else:
#             self.level=level
#
#     def attack(self):
#         return self.level*5
#
#
# class Soldier(Role):
#     def __init__(self,name,hurt):
#         super().__init__(name)
#         self.hurt=hurt
#     def attack(self):
#         return self.hurt
#
#
# class Team:
#     def __init__(self):
#         self.l=[]
#
#     def addMember(self,*member):
#         if len(self.l)+len(member)>6:
#             print('团队已满')
#         else:
#             self.l.extend(member)
#
#     def attack_sum(self):
#         self.sums=0
#         for i in self.l:
#             print(i.name,i.attack())
#             self.sums+=i.attack()
#         return self.sums
#
# t1=Team()
# t1.addMember(Magicer('jialing',5),
#              Magicer('xiaofeng',4),
#              Magicer('dengpeng',8),
#              Soldier('sas',200),
#              Soldier('dsfa',400),
#              Soldier('aad',1000)
#              )
# print(f'总伤害为{t1.attack_sum()}')

# 23.
# class Account:
#     def __init__(self,id,balance,pwd):
#         self.__id=id
#         self.__balance=balance
#         self.__pwd=pwd
#
#     def set_pwd(self,newAge):
#         if len(str(newAge))==6:
#             self.__pwd=newAge
#
#     def get_pwd(self):
#         return None
#
#
# class SavingAccount(Account):
#     def __init__(self,id,balance,pwd):
#         super().__init__(id,balance,pwd)
#
#     def interestRate(self,rate):
#         if 0<rate<0.1:
#             self.rate=rate
#         else:
#             self.rate=0.02
#
#
# class CreditAccount(Account):
#     def __init__(self,id,balance,pwd):
#         super().__init__(id,balance,pwd)
#
#     def creditLine(self,creditLine):
#         self.creditLine=creditLine

#24.
# class Shape:
#     def area(self):
#         pass
#     def girth(self):
#         pass
#
#
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#
#     def area(self):
#         return 3.14*self.r**2
#     def girth(self):
#         return 3.14*self.r*2
#
#
# class Rect(Shape):
#     def __init__(self, l,w):
#         self.l = l
#         self.w=w
#
#     def area(self):
#         return self.l*self.w
#
#     def girth(self):
#         return (self.l+self.w)*2
#
#
# class Square(Rect):
#     def __init__(self, a):
#         super().__init__(a,a)
#
#
# s=Square(5)
# print(s.area())
# print(s.girth())
# c=Circle(2)
# print(c.area())
# print(c.girth())
# r=Rect(2,3)
# print(r.area())
# print(r.girth())

#25.
# class Employee:
#     def __init__(self,name,birth):
#         self.__name=name
#         self.__birth=birth
#
#     def get_salary(self,month):
#         if self.__birth==month:
#             return 100
#         else:
#             return 0
#
#
# class SE(Employee):
#     def __init__(self,name,birth,salary):
#         super().__init__(name,birth)
#         self.__salary=salary
#
#     def get_salary(self,month):
#         return self.__salary+super().get_salary(month)
#
#
# class HE(Employee):
#     def __init__(self,name,birth,hours,rate):
#         super().__init__(name,birth)
#         self.__hours=hours
#         self.__rate=rate
#
#     def get_salary(self,month):
#         if self.__hours>160:
#             return (self.__hours-160)*self.__rate*1.5+160*self.__rate+super().get_salary(month)
#         else:
#             return self.__hours*self.__rate+super().get_salary(month)
#
#
# class SE2(Employee):
#     def __init__(self,name,birth,sales,rate):
#         super().__init__(name,birth)
#         self.__sales=sales
#         self.__rate=rate
#
#     def get_salary(self,month):
#         return self.__sales*self.__rate+super().get_salary(month)
#
#
# class BSE(SE2):
#     def __init__(self,name,birth,sales,rate,salary):
#         super().__init__(name,birth,sales,rate)
#         self.__salary=salary
#
#     def get_salary(self,month):
#         return self.__salary+super().get_salary(month)
#
#
# a=SE('jialing',10,10000)
# print(a.get_salary(10))
# b=HE('xiaofeng',9,300,20)
# print(b.get_salary(10))
# c=SE2('dengpeng',8,100000,0.05)
# print(c.get_salary(10))
# d=BSE('yangkun',12,5000,0.2,8000)
# print(d.get_salary(10))
#
# #26.
# l=[]
# l.extend([a,b,c,d])
# for i in l:
#     print(i.get_salary(10))

#27.
# class Stack:
#     def __init__(self):
#         self.stack=[]
#
#     def is_empty(self):
#         if self.stack:
#             return False
#         return True
#
#     def push(self,s):
#         self.stack.append(s)
#
#     def pop(self):
#         self.stack.pop()
#
#     def top(self):
#         return self.stack[-1]
#
#     def bottom(self):
#         return self.stack[0]
#
#
# a=Stack()
# a.push(1)
# a.push(2)
# print(a.top())
# print(a.bottom())
# print(a.is_empty())

#28.
# class Account:
#     def __init__(self,id,balance,pwd):
#         self.__id=id
#         self.__balance=balance
#         self.__pwd=pwd
#
#     def set_pwd(self,newAge):
#         if len(str(newAge))==6:
#             self.__pwd=newAge
#
#     def get_pwd(self):
#         return None
#
#
# class SavingAccount(Account):
#     def __init__(self,id,balance,pwd,rate):
#         super().__init__(id,balance,pwd)
#         self.rate=rate
#     def set_interestRate(self,rate):
#         if 0<rate<0.1:
#             self.rate=rate
#         else:
#             self.rate=0.02
#
#
# class CreditAccount(Account):
#     def __init__(self,id,balance,pwd,creditLine):
#         super().__init__(id,balance,pwd)
#         self.creditLine=creditLine
#
# class Bank:
#     def __init__(self):
#         self.l=[]
#     def openAccount(self,id,pwd,type,balance=0,rate=0.02,creditLine=-1000):
#         if type==0:
#             self.account=Account(id,balance,pwd)
#             self.l.append(self.account)
#         elif type==1:
#             self.account=SavingAccount(id,balance,pwd,rate)
#             self.l.append(self.account)
#         elif type==2:
#             self.account=CreditAccount(id,balance,pwd,creditLine)
#             self.l.append(self.account)
#         return self.account
#
#     def deposit(self,a,amount):
#         for i in self.l:
#             if i.id==a:
#                 i.balance+=amount
#         return i.balance
#
#     def withdraw(self,a,amount):
#         for i in self.l:
#             if i.id==a:
#                 if type(i)==CreditAccount:
#                     if i.balance-amount>=i.creditLine:
#                         i.balance-=amount
#                     else:
#                         print('额度不足')
#             else:
#                 if i.balance<amount:
#                     print('余额不足')
#                 else:
#                     i.balance-=amount


#29.
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
#
# class Line:
#     def getLen(self,p1,p2):
#         return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
#
#
# p1=Point(1,2)
# p2=Point(2,3)
# l1=Line()
# print(l1.getLen(p1,p2))