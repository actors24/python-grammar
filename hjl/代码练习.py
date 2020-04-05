# 字典
# 字典创建
# 1.直接创建
# dict1={'item1':'里好','item2':'李浩同桌'}
# print(dict1)
# print(type(dict1))

# dict1={}
# print(dict1)
# print(type(dict1))

# 2.利用工厂函数创建
# dict1=dict()
# print(dict1)
# print(type(dict1))

# dict(mapping)
# dict1=dict({'name':'jialing','age':22,'hobbies':['打游戏','半夜上厕所','去向不想']})
# print(dict1,type(dict1))

# dict1=dict(one=1,two=2,name='guojiguang',)
# print(dict1)

# dict(iterable)
# dict1=dict(['12','23'])
# dict1=dict([('name','654'),('date','sdf')])
# dict1=dict([['name','54'],['sdf','45']])
# dict1=dict([range(2)])
# print(dict1)

# print(range(2))
# # list1=[range(2),range(2),range(1,3)]
# # print(len(list1))

# a,b=12,23
# print(a,b)

# 模拟实现dict(iterable)
# d1={}
# list1=['12','34']
# for i in list1:
#     print(i)
# for a,b in list1:
#     print(a,b)
#     d1[a]=b
# print(d1)

# 键值对操作
# dict1={'name':'jialing','age':22,'lunch':'noodles'}
# # print(dict1['name'])
# # print(dict1['age'])
# # print(dict1["lunch"])
# # print(dict1['pb'])
#
# dict1['name']='jiaozi'
# print(dict1)
#
# dict1['salary']=10000
# dict1['salary']=20000
# print(dict1)
#
# del dict1['lunch']
# print(dict1)

# 字典遍历
# dict1={'name':'jialing','age':22,'lunch':'rice'}
# for i in dict1:
#     print(i,dict1[i])

# dict1={'name':'jialing','age':22,'lunch':'rice','hobbies':['学python','打球']}
# print(dict1)

# 增加
# dict1['addr']='沙河'
# print(dict1)
#
# print({'123':'123'})
# print({123:1234})
# print({123:True})
# print({123:[1,2,3]})
# print({True:(1,2,3)})
# print({(1,2,3):[1,2,3]})

# 字典常用方法
# #1.clear()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.clear()
# print(rst)
# print(dict1)

# 2.copy()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.copy()
# print(rst)
# print(dict1)

# 3.fromkeys()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.fromkeys([1,2,3,4],'193')
# print(rst)
# print(dict1)

# 4.get()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.get('name1','meizhaodao')
# # rst=dict1.get('name1')
# print(rst)
# print(dict1)

# 5.items() key() value()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst1=dict1.items()
# print(rst1)
# print(list(rst1))
# rst2=dict1.keys()
# print(rst2)
# print(list(rst2))
# rst3=dict1.values()
# print(rst3)
# print(list(rst3))

# 6.pop()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.pop('name','meizhaodao')
# print(rst)
# print(dict1)

# 7.popitem()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.popitem()
# print(rst)
# print(dict1)

# 8.setdefault()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst1=dict1.setdefault('name1')
# print(rst1)
# print(dict1)

# 9.update()
# dict1={'name':'jailing','age':22,'lunch':'rice'}
# rst=dict1.update(name='shanjie',age=20)
# print(rst)
# print(dict1)

# 集合创建
# set2={1,2,3,4,1,2,3,4,5,True,False,(1,2,3),'adsad'}
# print(set2,type(set2))

# set1={}
# print(set1,type(set1))

# 1.set
# set1=set()
# print(set1)

# 集合常用方法
# 1.add()
# set1={1,2,3}
# rst=set1.add(4)
# rst=set1.add(3)
# print(rst)
# print(set1)

# 2.clear()
# set1={1,2,3}
# print(set1.clear())
# print(set1)

# 3.discard()
# set1={1,2,3}
# print(set1.discard(1))
# print(set1)

# 4.pop()
# set1={'123',46,'sf',True,False}
# print(set1.pop())
# print(set1)

# 5.remove()
# set1={1,2,3}
# print(set1.remove(1))
# print(set1)

# 6.update()
# set1={1,2,3}
# print(set1.update([10,20]))
# print(set1.update({10,20},{30,40,50}))
# print(set1.update())
# print(set1)

# 7.difference()
# set1={1,2,3}
# print(set1.difference([2,3,0]))
# print(set1)

# 8.difference_update()
# set1={1,2,3}
# print(set1.difference_update({1,2,45}))
# print(set1)\

# 不可变集合
# 创建
# fset1 = frozenset()
# fset1 = frozenset((1, 2, 3, 5 , 4, 6, 7, 2, 2))
# fset1=frozenset({1:'one',2:'two'})
# fset1=frozenset('asfds')
# print(fset1, type(fset1))
#
# #对frozenset进行遍历操作
# print(list(fset1))
# for i in fset1:
#     print(i)

# union
# fset1=frozenset([1,2,3])
# fset2=frozenset([2,3,4,5,6])
# print(fset1.union(fset2))

# copy()
# fset1=frozenset([1,2,3])
# print(fset1.copy())

# 类
# 属性:名字 性别 年龄
# 方法:
# class Person:
#     name='jialing'
#     age=22
#     sex='male'
#     def eat(self,food):
#         print('I can eat',food)
#     def drink(self):
#         print('I can drink')
#     def sleep(self):
#         print('I can sleep')
#     def walk(self):
#         print('I can walk')
#
# #创建对象
# a=Person()
#
# #访问操作属性方法
# #访问属性 点语法
# print(a.name)
# print(a.age)
# print(a.sex)
#
# #方法访问 点语法
# a.eat('jiaozi')
# a.drink()
# a.sleep()
# a.walk()

# 类升级
# class Person:
#     # name='jialing'
#     # age=22
#     # sex='male'
#     def eat(self, food):
#         print('I can eat', food)
#
#     def drink(self):
#         print('I can drink')
#
#     def sleep(self):
#         print('I can sleep')
#
#     def walk(self):
#         print('I can walk')
#
#     def say(self, name, age, sex):
#         # 属性声明
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print('说话')


# 创建对象
# a = Person()
#
# # 访问操作属性方法
# # 访问属性 点语法
# a.say('xiaofeng', 33, 'famale')
# print(a.name)
# print(a.age)
# print(a.sex)
# #__dict__检测成员
# print(a.__dict__)
#
# #修改实例属性
# a.age=30
# print(a.age)

# class Dog:
#     name='大荒'
#     def bark(self):
#         self.sleep='dsfsdf'
#         self.age=2
#         print('汪汪汪',self.name,self.age)
#     def sleep(self):
#         print('afsfgf')

# a=Dog()
# print(a.name)
# print(a.__dict__)
# a.bark()
# print(a.bark)
# print(a.__dict__)
# a.bark()
# print(a.name)
# print(a.age)

# a.name='wangcai'
# print(a.name)
# print(a.__dict__)
#
# b=Dog()
# print(b.name)
# a.bark()
# print(a.sleep)
# a.bark()

# self
# class Cat:
#     name='必死'
#     def eat(self):
#         self.name='sdf'
#         print(self.name)
#         print('吃鱼')
#     def bark(self):
#         print(self.name)
#         print('喵喵秒')
#
# Cat().bark()
# # Cat.bark()
# # Cat.eat()
# Cat.bark(cat1)

# init方法
# class Pig:
#     name='ada'

# 类的继承与方法重写
# class Person:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#
# class Work:
#     def __init__(self,time,salary):
#         self.time=time
#         self.salary=salary
#     def speak(self):
#         print(f'时间为{self.time},工资为{self.salary}')
#
#
# class Student(Person):
#     def __init__(self,name,age,sex,grade):
#         Person.__init__(self,name,age,sex)
#         self.grade=grade
#     def speak(self):
#         print('我是父类')
#
#
# class Career(Work,Student):
#     def __init__(self,name,age,sex,grade,time,salary):
#         Student.__init__(self,name,age,sex,grade)
#         Work.__init__(self,time,salary)
#
#     def career(self):
#         print(f'我叫{self.name},我今年{self.age}岁了,性别{self.sex},成绩{self.grade},学习时间为{self.time},工资为{self.salary}')
#     def speak(self):
#         print('我是子类')
#
# a=Career('黄嘉灵',22,'男',100,14,10000)
# a.speak()
# super(Career,a).speak()

# 类的私有属性
# class JustCount:
#     __privatePwd=0
#     publicPwd=0
#     def count(self):
#         self.__privatePwd+=1
#         self.publicPwd+=2
#         print('私有密码为:',self.__privatePwd)
#         print('共有密码为:',self.publicPwd)
#
#
# a=JustCount()
# a.count()
# a.count()
# print(a.publicPwd)
# #实例不能访问私有属性
# print(a.__privatePwd)

# 类的私有方法
# class Site:
#     def __init__(self, name, url):
#         self.name = name
#         self.url = url
#
#     def info(self):
#         print(f'name:{self.name}')
#         print(f'url:{self.url}')
#
#     def public(self):
#         print('这是公有方法')
#         self.__private()
#
#     def __private(self):
#         print('这是私有方法')
#
#
# a = Site('百度', 'www.baidu.com')
# a.info()
# a.public()
# # a.__private()

# class ClassName:
#     @staticmethod
#     def fun():
#         print('静态方法')
#
#     @classmethod
#     def a(cls):
#         print('类方法')
#
#     def b(self):
#         print('普通方法')
#
# ClassName.fun()
# ClassName.a()
# ClassName.b()

# 运算符重载
# class Vector:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def __repr__(self):
#         return 'Vector (%d,%d)'%(self.a,self.b)
#
#     def __add__(self, other):
#         return Vector(self.a+other.a,self.b+other.b)
#
# v1=Vector(1,2)
# v2=Vector(3,4)
# print(v1+v2)

# class Person:
#     name='jiasling'
#     age=22
#     def info(self):
#         print(f'我叫{self.name},今年{self.age}岁了')
#     def name(self):
#         print('哈哈')
#
#
# p1=Person()
# p1.info()
# print(p1.name)

# 接口
# def fun(n):
#     print(n.he)
#
#
# class A:
#     he='ssffd'
#
#
# a=A()
# fun(a)

# a='abc'
# b,c='b','c'
# [d,e]=['d','e']
# f,g='fg'
# h,*i='sfgg'
# j=k=l='l'
# print(a,b,c,d,e,f,g,h,i,j,k,l)

# class Person:
#     name='dhg'
#     def abc(self):
#         # self.name=18
#         self.name='sdfs'
#         print(self.name)
#
# # a=Person()
# # a.abc()
# b=Person()
# b.abc()

# class Girl:
#     __age=18
#     def get_age(self):
#         return self.__age
#
# g=Girl()
# print(g.get_age())

# class Girl:
#     def __init__(self):
#         self._age = 280
#
# g=Girl()

# print(list(filter(lambda x:x,range(5))))
# print(list(map(lambda x,y:x+y,[1,2,3],[3,4,5])))
# import functools
# print(functools.reduce(lambda x,y:x*y,[1,2,3,4,5],2))

# import sys
#
# print('命令行参数如下：')
# for i in sys.argv:
#     print(i)
#
# print('\n\nPython路径为：',sys.path,'\n')

# print(__name__)
# if __name__=='__main__':
#     print('hehe')
#
# class A:
#     def __hehe(self):
#         print('nihao')
#
#
# a=A()
# a.__hehe()

