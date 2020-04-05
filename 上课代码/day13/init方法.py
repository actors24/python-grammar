
# __init__() python 特殊方法 魔法方法 构造方法 初始化方法

class Pig:
    # name = '佩奇'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say(self):
        print(f'我叫{self.name}')
    def eat(self,food):
        print(f'我喜欢吃{food}')

pig1 = Pig('乔治',2)
pig2 = Pig('佩奇',2)
print(pig1.name)
print(pig2.name)

pig1.eat('私聊')

