#module01
# a=10
#
# def fn():
#     print('我是module01中的fn函数')
#
# class A:
#     name='module01_A'
#
#     def a_fn(self):
#         print('我是class A中的a方法')
#     def __hehe(self):
#         print('hehe')
#
#
# # print(__name__)
#
# if __name__=='__main__':
#     print('我是module01的打印语句')

#module02
# import module01 as a
#
# print(a.a)
#
# a = 20
#
# print(a)
#
# import module01 as a
#
# print(a.a)
# print(a)
#
#
# def fn():
#     print('我是module02中fn')
#
#
# a.fn()
# fn()

#module03
# b=30
#
# def module03():
#     print('我是module03')
#
# class B:
#     name='module03'
#
#     def b(self):
#         print('我是B类中的b函数')

#module04
# import module01,module03
#
# module03.module03()

# import module03 as a
# a.module03()

# import module01 as a,module03 as aa
#
# aa.module03()
# print(a.a)
# aa.fn()
#
# from userapp import module05
#
# module05.module05()
# print(module05.c)
# module05.C()

# from userapp.migrations import module06
#
# print(module06.e)

#module05
# c=100
#
# def module05():
#     print('我是module05中函数')
#
#
# class C:
#     name='module05'
#
#     def c_fn(self):
#         print('我是C类中的c_fn函数')
#

#module06
# e='module06'

# from orderapp import module07
#
# print(module07.f)

#module07
# f='module07'

# from userapp.migrations import module06
#
# print(module06.e)

#module08
# g='module08'
#
# import module07
#
# print(module07.f)

#module09
# from orderapp import module07 as usb,module08 as usa
#
# print(usa.g)
# print(usb.f)

# import orderapp

# print(orderapp)
# print(orderapp.name)
#
# import orderapp.module07 as ufo,orderapp.module08 as ofo
#
# print(ufo.f)
# print(ofo.g)

#time10
import time

#1.sleep(seconds)
# print(123)
# time.sleep(5)
# print(456)

#2.strftime()
# print(time.strftime('%Y-%m-%d %H:%M-%S'))

#3.localtime()
# print(time.localtime())

#4.time()
# print(time.time())