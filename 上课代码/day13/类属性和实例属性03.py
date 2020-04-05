
#
class Dog:
    # 类属性
    name = '大黄'

    # 方法
    def jiao(self):
        self.sleep = '随便凑数的'
        self.age = 2
        # name = '小强'
        print(f'旺旺旺,我叫{self.name},我今年{self.age}岁了')
    def sleep(self):
        print('狗睡觉')

# 创建实例对象
dog1 = Dog()
# print(dog1.name)
# print(dog1.__dict__)
# dog1.jiao()
# print(dog1.age) # 2
# print(dog1.__dict__) # {'age': 2}


#
# dog1.jiao()
# print(dog1.name)

# 修改
# dog1.name = '旺财'
# print(dog1.name)
# print(dog1.__dict__) # {'name': '旺财'}
# #
# dog2 = Dog()
# print(dog2.name)

#
# print(dog1.jiao)
# dog1.jiao()
#
# dog1.jiao()
# print(dog1.jiao)


#

# dog1.jiao()
# dog1.sleep()
# print(dog1.sleep) # 随便凑数的


#
dog1.jiao()





