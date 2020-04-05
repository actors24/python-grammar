# class Animal:
#     def eat(self):
#         print('animal can eat')
#
# class Dog(Animal):
#     pass
#
#
# d=Dog()
# d.eat()

class Father:
    __money=1000000
    # def __init__(self):
    #     print('我是亲爹')
    def drink(self):
        print('爸爸喜欢喝酒')
    # def get_money(self):
    #     return self.__money

class Kid(Father):
    # def __init__(self):
    #     print('我是儿子')
    def drink(self):
        print('儿子喜欢喝酒')

class Boss:
    money=1000000

class Girl(Father,Boss):
    pass

k=Kid()
# print(k.money)
k.drink()
g=Girl()
print(g.money)














