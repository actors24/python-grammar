class Animal:
    def eat(self):
        print('animal can eat')

class Dog(Animal):
    def eat(self):
        print('dog eat bone')

class Monkey(Animal):
    def eat(self):
        print('monkey eat banana')

class Machine:
    def work(self):
        print('machine can work')

class Robot(Machine,Animal):
    pass

def fun(animal): # 传入父类的多种形态（子类）
    animal.eat()


monkey=Monkey()
fun(monkey)
robot=Robot()
fun(robot)

