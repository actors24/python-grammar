"""
@File    :   zuhe.py
@Author  :   zhouJunFeng    
@Contact :   zx051225@163.com
@Modify Time :   2019/12/14 21:41
"""


# class Point:
#     """点类"""
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Line:
#     """线类"""
#
#     def __init__(self, p1, p2):
#         self.p1 = p1  # 点类的实例对象p1
#         self.p2 = p2  # 点类的实例对象p2
#
#     def get_len(self):
#         return ((self.p1.x - self.p2.x) ** 2 + (
#                 self.p1.y - self.p2.y) ** 2) ** 0.5
#
#
# # 在类外 构造出被包含类的实例对象
# p1 = Point(1, 1)
# p2 = Point(4, 5)
# line1 = Line(p1, p2)  # 将点类的对象作为参数传给线类的构造方法
# print(line1.get_len())
#
#
#
# class Turtle(object):
#     """乌龟类"""
#
#     def __init__(self, x):
#         self.num = x
#
#
# class Fish(object):
#     """鱼类"""
#
#     def __init__(self, y):
#         self.num = y
#
#
# class Pool(object):
#     def __init__(self, turtle_num, fish_num):
#         self.turtles = Turtle(turtle_num)
#         self.fishs = Fish(fish_num)
#
#     def show_pool(self):
#         print(f'池子里有{self.turtles.num}只乌龟，有{self.fishs.num}条鱼')
#
# # 在类中构造出被包含对象的实例对象
# pool = Pool(3,5)
# pool.show_pool()
#
#
#
#
#
#
#
# class Role:
#     """角色"""
#
#     def __init__(self, name):
#         self.__name = name
#
#     @property               #get
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         self.__name = name
#
#     def attack(self):
#         pass
#
#
# class Magicer(Role):
#     """魔法师"""
#
#     def __init__(self, name, magic_lv):
#         super().__init__(name)
#         if 10 >= magic_lv >= 1:
#             self._magic_lv = magic_lv
#         else:
#             print('魔法师等级error')
#             self._magic_lv = 1
#
#     def attack(self):
#         return self._magic_lv * 5
#
#
# class Solider(Role):
#     """战士"""
#
#     def __init__(self, name, hurt):
#         super().__init__(name)
#         self._hurt = hurt
#
#     def attack(self):
#         return self._hurt
#
#
# class Team:
#     """打怪小队"""
#
#
#     def __init__(self):
#         self._team = []
#
#     def add_member(self, *roles):
#         if len(self._team) + len(roles) <= 6:
#             self._team.extend(roles)
#         else:
#             print('小队人员已满')
#
#     def attack_sum(self):
#         self._attack_sums = 0
#         for i in self._team:
#             self._attack_sums += i.attack()
#         return self._attack_sums
#
#
# role = Role('DDD')
# print(role.name)
# role.name = 'asdsa'
# print(role.name)
# magicer = Magicer('zx',6)
# print(magicer.name)
#
#
# # team1 = Team()
# # team1.add_member(Magicer('m1', 10),  # 等级10 伤害50
# #                  Magicer('m2', 9),  # 等级9  伤害45
# #                  Magicer('m3', 1),  # 等级1  伤害5
# #                  Solider('s1', 100),  # 伤害 100
# #                  Solider('s2', 10),  # 伤害 10
# #                  Solider('s3', 120))  # 伤害 120
# # print(team1.attack_sum())
#
#
#
#
#
#
#
# # # 18.解决方法：使用super()方法
# class A:
#     def __init__(self):
#         print('进入A')
#
#         print('离开A')
#
#
# class B(A):
#     def __init__(self):
#         print('进入B')
#         A.__init__(A)
#         print('离开B')
#
#
# class C(A):
#     def __init__(self):
#         print('进入C')
#         A.__init__(A)
#
#         print('离开C')
#
#
# class D(B, C):
#     def __init__(self):
#         super().__init__()
#
#
# d = D()
# print(D.mro())


# class A(object):
#     def __init__(self,name):
#         self.name = name
#
#
# class B(A):
#     pass
#
#
# b = B('ZX')
# print(b.__dict__)
# print(A.__dict__)

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
class E(B):
    pass
class F(C):
    pass
class G(C):
    pass
class H(D,E):
    pass
class I(E,F):
    pass
class J(F,G):
    pass
class K(H,I,J):
    pass

print(K.mro())


