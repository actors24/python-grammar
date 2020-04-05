# import sys


class Person:
    # 三个属性
    # name = '李老板'
    # age = 99
    # sex = '女'
#     方法
    def eat(self,food):

        print(f'吃{food}')
    # 说
    def say(self,name,age,sex):
        # 属性声明
        self.name = name
        self.age = age
        self.sex = sex
        print('说话')

p1 = Person()
p1.say('李伟东',25,'女')
print(p1.name)
print(p1.age) #
print(p1.sex)  # AttributeError 属性


p2 = Person()
p2.say('孔夫子',30,'男')
print(p2.name)
print(p2.age)  # 30
print(p2.sex)  # AttributeError 属性

# __dict__ 检测 成员
print(p1.__dict__)
print(p2.__dict__)


# 修改 实例属性
p2.age = 30
print(p2.age) # 30

# 再次访问 p1 的age属性
print(p1.age) # 25