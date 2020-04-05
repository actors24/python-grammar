# 组合
# class B:
#     hehe=100
#
# class A:
#     age=10
#     b=B()
#
#
# a=A()
# print(a.age)
# print(a.b.hehe)

# class Teacher:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# 1.类属性 组合
# class School:
#     teacher=Teacher('xiaobo',40)
#     student=Student('jiangang',18)
#
#
# a=School()
# print(a.teacher.name)
# print(a.student.name)

# 2.实例属性 组合
# class School:
#     def kai_xue(self,t_name,t_age,s_name,s_age):
#         self.teacher=Teacher(t_name,t_age)
#         self.student=Student(s_name,s_age)
#
#
# a=School()
# a.kai_xue('xiaobo',40,'jiangang',18)
# print(a.teacher.name)
# print(a.student.name)

# 3.实例属性 组合
# class School:
#     def kai_xue(self):
#         self.teacher=Teacher('xiaobo',40)
#         self.student=Student('jiangang',18)
#
#
# a=School()
# a.kai_xue()
# print(a.teacher.name)
# print(a.student.name)

# 4.
# class School:
#     def __init__(self,t_name,t_age,s_name,s_age):
#         self.teacher=Teacher(t_name,t_age)
#         self.student=Student(s_name,s_age)
#
#
# a=School('xiaobo',40,'jiangang',18)
# print(a.teacher.name)
# print(a.student.name)

# 5.
# class School:
#     def __init__(self,teacher,student):
#         self.teacher=teacher
#         self.student=student
#
# a=School(Teacher('xiaobo',40),Student('jiangang',18))
# print(a.teacher.name)
# print(a.student.name)

# 命名冲突
# class A:
#     age=18
#     def age(self):
#         print('hehe')
#
#
# a=A()
# a.age()

# class A:
#     def age(self):
#         age=18
#         print(age)
# #
#
# a=A()
# a.age()
# print(a.age)

# class A:
#     def age(self):
#         self.age=20
#         print(self.age)
#
#
# a=A()
# a.age()
# print(a.age)
# del a.age
# print(a.age)

# 私有化
# class Girl:
#     __age=28
#     def get_age(self):
#         return self.__age
#     def __hehe(self):
#         print('hehe')
#     def set_age(self,newAge):
#         self.__age=newAge
#
#
# g=Girl()
# # print(g.__age)
# print(g.get_age())
# g.set_age(20)
# print(g.get_age())

# class Girl:
#     def __init__(self):
#         self.__age=28
#
#
# g=Girl()
# print(g._Girl__age)

# class Animal:
#     def eat(self):
#         print('Animal can eat')
#
# class Dog(Animal):
#     pass
#
#
# d=Dog()
# d.eat()

# class Father:
#     __money=1000000
#     def __init__(self):
#         print('我是亲爹')
#     def drink(self):
#         print('爸巴喜欢喝酒')
#     def get_money(self):
#         return self.__money
#
#
# class Kid(Father):
#     def __init__(self):
#         print('我是儿子')
#     def drink(self):
#         print('儿子喜欢喝酒')
#
#
# class Boss:
#     mpney=1000000
#
#
# class Girl(Father,Boss):
#     pass
# k=Kid()
# k.drink()
# print(k.get_money())
# g=Girl()
# print(g.mpney)

# 多继承
# class Father:
#     money=1000000
#
#
# class StepFather:
#     money=10000
#
#
# class Son(Father,StepFather):
#     pass
#
#
# s=Son()
# print(s.money)

# 循环继承问题
# class Grangpa():
#     pass
#
#
# class Father(Grangpa):
#     pass
#
#
# class Son(Father,Grangpa):
#     pass
#
#
# s=Son()

# 钻石继承问题
# class Grandpa:
#     def __init__(self):
#         super().__init__()
#         print('我是爷爷')
#
# class Father(Grandpa):
#     def __init__(self):
#         super().__init__()
#         print('我是爸爸')
#
#
# class Uncle(Grandpa):
#     def __init__(self):
#         super().__init__()
#         print('我是叔叔')
#
#
# class Son(Father,Uncle):
#     def __init__(self):
#         super().__init__()
#         print('我是儿子')
#
#
# s=Son()
# print(Son.mro())
# print(Grandpa.mro())