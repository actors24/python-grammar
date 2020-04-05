# class Student:  # Student--类名--元对象(描述类）
#     # 属性
#     # 方法
#     name = '小明'
#     age = 18
#     sex = 'male'
#     id = '007'
#
#     # 方法
#     def learn(self):
#         # 实例属性
#         self.name = '小黑'
#         name = '呵呵'
#         print(name)
#         print(self.name)
#         print('I love learn')
#
#     def eat(self):
#         print('I can eat')
#
#     def sleep(self):
#         print('I want to sleep')
#
#
# # s=Student()
# # print(s.name)
# # print(s.age)
# # print(s.sex)
# # s.eat()
# # s.learn()
# s1 = Student()
# # print(s1.name)
# # print(Student.name)
# # s1.name='DAMING'            #实例属性
# # print(s1.name)
# # print(Student.name)
#
# s3 = Student()
# s4 = Student()
#
# print(s3.name, s4.name)
# s3.learn()
# print(s3.learn(), s4.learn())
# print(Student.name)

# class A:
#     age=18
#     def hehe(self.n):
#         self.age=n
# a1=A()
# # print(a1.age)
# # a1.age=20
# # print(a1.age)
# # print(A.age)
# a1.hehe(20)
# print(A.age)
# print(a1.age)

# class A:
#     age=18
#     def fun(self):
#         self.age=99
#         print('hehe',self.age)
# a1=A()
# a1.fun(a1)
# a1.age=99
# # a1.age=99
# # a1.fun()
# # print(a1.age)
# # a2=A()
# # a2.age=199
# # a2.fun()

# def fun(name,age=18,*hobbies,**kwargs):
#     print(f'我叫{name},今年{age}岁了,我的爱好是{hobbies},其他由{kwargs}')
#
# fun('黄嘉灵',18,'唱歌','打球',other1='1',other2='2')

# a='welcome to baizhi ab ba we th'
# b=a.split(' ')
# for i in range(len(b)//2):
#     b[i],b[len(b)-i-1]=b[len(b)-i-1],b[i]
# print(b)
# def fun1():
#     def fun2():
#         return True
#
#     print(fun2())
#
# print(fun1())

# a=[2,3,1,4,6,5,7,8]
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j]<a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

class Card:
    __pwd = '123'

    def getPwd(self):
        return self.__pwd

    def setPwd(self, newPwd):
        self.__pwd = newPwd


c = Card()
c.setPwd('789')
print(c.getPwd())
print(c._Card__pwd)

# class Dog():
#     age=4
#     def __init__(self):
#         print(self.age)
#
# black=Dog()
# import functools
# a=functools.reduce(lambda x,y:x*2+y,[1,2,0],10)
# print((a))
