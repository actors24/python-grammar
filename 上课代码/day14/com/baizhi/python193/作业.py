# class Person:
#     def __init__(self,name='飞哥',age=18):
#         self.name=name
#         self.age=age
#
#
#
# p1=Person()
# p2=Person('小波',40)
# p3=Person('建刚',18)
#
# print(p1.name)
# print(p2.name)
# print(p3.name)


# class Worker:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def work(self,time):
#         pass
#
# w1=Worker()
# w2=Worker()
# w3=Worker()

# # 9
# class Ticket:
#     # 2个成人，1个小孩的票价
#     price=100
#     def hehe(self,zhou,chengren,xiaohai):
#         if 7>=zhou>=6:
#             # 120%
#             print((chengren * self.price + xiaohai * self.price * 0.5)*1.2)
#         else:
#             print(chengren*self.price+xiaohai*self.price*0.5)
#
# t=Ticket()
# t.hehe(5,2,1)
# t.hehe(6,2,1)


# class Ticket:
#     def __init__(self,week,adult,kid):
#         self.week=week
#         self.adult=adult
#         self.kid=kid
#     def get_price(self):
#         if 7>=self.week>=6:
#             print((self.adult * 100 + self.kid * 50)*1.2)
#         else:
#             print(self.adult*100+self.kid*50)
#
#
# t=Ticket(5,2,1)
# t.get_price()
# t2=Ticket(6,2,1)
# t2.get_price()




class Address:
    def __init__(self,address,zipCode):
        self.address=address
        self.zipCode=zipCode

class Worker:   # 思路： 按需供应
    def __init__(self,name,age,salary,address,zipCode):
        self.name=name
        self.age=age
        self.salary=salary
        self.addr=Address(address,zipCode) # 分门别类

w1=Worker('zhang3',25,2500,'北京市海淀区清华园1号','100084')
print(w1.addr.address)















