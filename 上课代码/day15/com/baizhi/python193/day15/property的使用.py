class A:
    def __init__(self):
        self.__age=18

    def get_age(self):
        return self.__age

    def set_age(self,newAge):
        self.__age=newAge

    def del_age(self):
        del self.__age

    x=property(fget=get_age,fset=set_age,fdel=del_age,doc='hehe') # property对象

a=A()
# print(a.get_age())
print(a.x)  # 访问---fget()  get_age()
a.x=100  # 赋值 ---fset(100)   set_age(100)
print(a.x)
print(a._A__age)
# del  a.x  # 删除 --- fdel()  del_age()
# print(a.get_age())
a.set_age(200)
print(a.x)




