# 不可变集合
# 创建
# fset1=frozenset()
# print(fset1,type(fset1))

# fset1=frozenset([1,2,3,1,2,3,4])
# fset1=frozenset((1,2,3,12,4,4))
# fset1=frozenset('afddf13')
# fset1=frozenset({'name':'jialing','age':'male'})
# fset1=frozenset(range(5))
# print(fset1)
# for i in fset1:
#     print(i)

# union 并集
# fset1=frozenset([1,2,3])
# fset2=frozenset([1,4,5,3,65])
# print(fset1.union(fset2))
# print(fset2)
# print(fset1)

# 类创建
# 人类
# 属性:名字,年龄,性别
# 方法:吃,喝,睡,走
# class Person:
#     #三个属性
#     name='jialing'
#     age=22
#     sex='male'
#     #方法
#     def eat(self,food):
#         print(f'吃{food}')
#
#
# #创建对象
# p1=Person()
# print(p1)
# print(type(p1))
# #访问属性
# print(p1.name)
# print(p1.age)
# print(p1.sex)
#
# #方法访问
# p1.eat('jiaozi')
# #查看p1对象所有成员
# print(p1.__dict__)

# class Person:
#     #三个属性
#     name='jialing'
#     age=22
#     sex='male'
#     #方法
#     def eat(self,food):
#         print(f'吃{food}')
#     #说
#     def say(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         print('说话')
#
#
# p1=Person()
# p1.say('weidong',25,'male')
# print(p1.name)
# print(p1.age)
# print(p1.sex)
#
# p2=Person()
# p2.say('xiaofeng',21,'male')
# print(p2.name)
# print(p2.age)
# print(p2.sex)
#
# #检测成员
# print(p1.__dict__)
# print(p2.__dict__)
#
# p2.age=23
# print(p2.age)
# print(p2.__dict__)
#
# print(p1.age)

# 类属性和实例属性
# class Dog:
#     #类属性
#     name='dahuang'
#     #方法
#     def jiao(self):
#         self.sleep='suibian'
#         self.age=2
#         self.name='xiaoqiang'
#         print(f'汪汪汪,我叫{self.name},我今年{self.age}岁了')
#     def sleep(self):
#         print('狗睡觉')


# 创键实例对象
# dog1=Dog()
# print(dog1.name)
# print(dog1.__dict__)
# dog1.jiao()
# print(dog1.age)
# print(dog1.__dict__)

# 修改
# dog1.name='wangcai'
# print(dog1.name)
# print(dog1.__dict__)
#
# dog2=Dog()
# print(dog2.name)
#
# print(dog1.jiao)
# dog1.jiao()
#
# dog1.jiao()
# print(dog1.jiao)

# dog1.jiao()
# dog1.sleep()
# print(dog1.sleep)

# 方法
# class Cat:
#     name='波斯'
#     def eat(self,val):
#         self.name=val
#         print(self.name)
#         print('吃鱼')
#     def jiao(self):
#         print('喵喵喵')
#         print(self.name)
#
#
# cat1=Cat()
# # print(cat1)
# # cat1.eat('jialing')
# # print(cat1.name)
# #
# # #类访问类属性
# # print(Cat.name)
# # cat1.eat('xiaofeng')
# # print(Cat.name)
#
# cat1.eat('dahuang')
# print(cat1.name)
# Cat().eat('xiaohei')
# print(cat1.name)
#
# Cat().jiao()

# student_list = [
#     ['李伟东','193班',507,'python班级'],
#     ['张三','190班',506,'java班级'],
#     ['王老师','508办公室',508,'办公室'],
# ]
#
# class Member:
#     #属性
#     def __init__(self,name,classnum,roomnum,note):
#         self.name=name
#         self.classnum=classnum
#         self.roomnum=roomnum
#         self.note=note
#         #方法
#     def intro(self):
#         print(self.name,self.classnum,self.roomnum,self.note)
#
# mem1=Member('李老板','193班',507,'python班级')
# mem1.intro()

# __init__()
# class Pig:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def say(self):
#         print(f'我叫{self.name}')
#     def eat(self,food):
#         print(f'我喜欢吃{food}')
#
#
# pig1=Pig('乔治',2)
# pig2=Pig('佩奇',2)
# print(pig1.name)
# print(pig2.name)
# pig1.eat('饲料')
# pig1.say()
