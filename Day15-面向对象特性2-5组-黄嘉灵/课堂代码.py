# #多态
# class Animal:
#     def eat(self):
#         print('animal can eat')
#
#
# class Dog(Animal):
#     def eat(self):
#         print('Dog can eat')
#
# class Monkey(Animal):
#     def eat(self):
#         print('monkey can eat')
#
# class Machine:
#     def work(self):
#         print('machine can work')
#
#
# class Robot(Machine,Animal):
#     pass
#
#
# def fun(animal):    #传入父类的多种形态（子类）
#     animal.eat()
#
#
# dog=Dog()
# fun(dog)
# monkey=Monkey()
# fun(monkey)
# robot=Robot()
# fun(robot)

# 常用函数
# class A:pass
# class B:pass
# class C(A):
#     age=18

# print(issubclass(C,A))
# print(issubclass(C,B))
# print(issubclass(C,(A,B)))

# c=C()
# print(isinstance(c,C))
# print(isinstance(c,B))
# print(isinstance(c,(A,B)))

# c=C()
# print(hasattr(c,'age'))
# print(hasattr(c,'name'))
# print(getattr(c,'age'))
# print(getattr(c,'hehe','age'))
# setattr(c,'name','jialing')
# print(c.name)
# print(getattr(c,'name'))
# delattr(c,'name')
# print(c.name)

# property的使用
# class A:
#     def __init__(self):
#         self.__age=18
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self,newAge):
#         self.__age=newAge
#
#     def del_age(self):
#         del self.__age
#
#
#     x=property(fget=get_age,fset=set_age,fdel=del_age,doc='sdfgsdfg')
#
#
# a=A()
# print(a.get_age())
# print(a.x)
# a.x=100
# print(a.x)
# print(a.get_age())
# # del a.x
# # print(a.x)
# # print(a.get_age())
# a.set_age(20)
# print(a.x)
# print(a.get_age())
