
# self

class Cat:
    name = '波斯'

    def eat(self,val):
        self.name = val
        print(self.name) # cat1.name
        print('吃鱼')
    def jiao(self):
        print('喵喵喵。。。。。。')
        print(self.name)

# cat1 = Cat()
# # print(cat1,'14行')
# cat1.eat()
# print(cat1.name)

# 类访问 类属性
# print(Cat.name) # 波斯
# cat1.eat()
# print(Cat.name) # 波斯

# 类访问方法
# Cat.jiao(10)
# Cat.eat(cat1)
# print(cat1.__dict__)

# cat1 = Cat()
# cat1.eat('大黄')
# print(cat1.name)
#
# Cat().eat('小黑')
#
# print(cat1.name) # 大黄

# Cat().eat('大黄')
# Cat().eat('小黑')
# Cat().eat('小白')
# Cat().jiao()





