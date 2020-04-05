"""
@File    :   protected2.py
@Author  :   zhouJunFeng    
@Contact :   zx051225@163.com
@Modify Time :   2019/12/14 20:52
"""
class A:
    _p = '2_protected_attr'
    p = '2_public_attr'
    __p = '2_private_attr'

    def protected(self):
        print(self._p)

    def public(self):
        print(self.p)

    def private(self):
        print(self.__p)

    def get_private(self):  #get
        print(self.__p)

    def set_private(self,value):# set
        self.__p = value

    xx = property(get_private,set_private)
#
a = A()

# # print(a.p)
# # a.public()
# # print(a._p)
# # a.protected()
# # # print(a.__private_attr)
# # print(a._A__p)
# # a.private()
# # print(A.__dict__)
# # print(a.get_private())
# # print(a.xx)
# a.xx = 'hl'
# print(a._A__p)
# a.xx
# print(a.xx)
# print(A._A__p)


# class B(A):
#     pass
#
# b = B()
# print(b._p)
# print(b.p)
# print(b._A__private_attr)

# import property1
# p1=property1
# print(p1.A.p)
# print(p1.A._p)
# # print(p1.A.__private_attr)
# print(p1.A._A__p)
# print(p1._num)
#

num = 2
print(num)
breakpoint()
print(num)
from property1 import *
from zuhe import *

# 自动过滤以_开头的属性
# print(A.public_attr)
# print(A._protected_attr)
# # print(A._A__private_attr)
print(num)
# print(_num)
# print(__num)
print(num)
num =3
print(num)









