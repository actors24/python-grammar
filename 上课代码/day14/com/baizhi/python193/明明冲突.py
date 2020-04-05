# class A:
#     age=18
#     def age(self):  # 方法名，本质也是个变量名
#         print('hehe')
#
# a=A()
# a.age()

# class A:
#     def age(self):
#         age=18  # 局部变量 --- 局部变量用一次后就会自动消失
#         print(age)
#
# a=A()
# a.age()
# print(a.age)


# class A:  # 类属性： 类属性  方法     实力属性
#     def age(self):
#         self.age=20
#         print(self.age)
#
# a=A()
# a.age()
# print(a.age)
# del a.age
# print(a.age)


class A:
    def __init__(self):
        print('hehe')


a=A()
a.__init__()
















