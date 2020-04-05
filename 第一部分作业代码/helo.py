# print(int(-1.6))

# a = int(input('请输入年龄:'))
# if 0 < a <= 4:
#     print('改年龄段为婴儿')
# elif 5 < a < 13:
#     print('该年龄段为儿童')
# elif 13 <= a < 18:
#     print('该年龄段为儿童')
# elif 18 <= a < 35:
#     print('该年龄段为青年')
# elif 35 <= a < 65:
#     print('该年龄段为中年')
# elif a >= 65:
#     print('改年龄段为老年')


# while 1:
#     a = int(input('请输入一个数:'))
#     sums=1
#     for i in range(1, a+1):
#         sums *= i
#     print(f'该数的阶乘为{sums}')

# assert 1 > 1

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(a.index(4))
# b = a[2:-2]
# b = a[1:]
# b = a[-1:4:-1]
# b = a[2:-1:-1]
# b = a[5:0:-1]
# b = a[5::-1]
# print(b)

# a = [1, 2, 3, 4]
# a.sort(reverse=True)
# print(a)
#
# a.reverse()
# print(a)

# t = [1, 2, [3, 4]]
# for i in t:
#     if isinstance(i, list):
#         for j in i:
#             print(j)

# t = [3, 4, 2, 6, 8, 1, 7, 5]

# for i in range(len(t)-1):
#     for j in range(len(t)-i-1):
#         if t[j] > t[j+1]:
#             t[j], t[j+1] = t[j+1], t[j]
#
# print(t)

# for i in range(len(t)-1):
#     for j in range(i+1,len(t)):
#         if t[i]>t[j]:
#             t[i], t[j] = t[j], t[i]
#
# print(t)

# t = 'as黄dadaJHd'
# a = '23123三'
# b = ' a     '
# print(t.count('a', 1, 5))
# print(t.find('b'))
# print(t.index('d'))
# print(t.capitalize())
# print(t)
# print(t.casefold())
# print(t.lower())
# print(t.upper())
# print(t.isalpha())
# print(a.isnumeric())
# print(a.isdigit())
# print(t.islower())
# print(t.isupper())
# print(b.isspace())
# print(t.center(20, '*'))
# print(t.ljust(20, '&'))
# print(t.rjust(20, '@'))
# print(t.replace('a', 'z'))
# print(t.replace('a', 'z', 1))
# print(t.split('a'))
# print(b.strip())
# print(a.endswith('a'))
# print(t.endswith('A'))
# print(b.endswith(''))
# print(t.startswith('a'))
# print(t.startswith(''))
# print(t.encode())
# print(t)
# print(t.encode().decode())
# print('@'.join(t))
# print(a.swapcase())
# print(t.swapcase())

# a = '我叫{a},今年{b}岁了'
# print(a.format(a='jialing', b=22))

# s = 'Adasdasd'
# a = [1, 2, 3, 4, 6]
# print(max(s))
# print(min(s)
#       )
# print(sum(a, 10))
# print(list(reversed(s)))
# print(sorted(s))
# print(sorted(a, reverse=True))
# print(list(zip(s, a)))
# print(list(enumerate(s, 2)))

# def f1(a):
#       a()
#
#
# def a():
#       print('aaaa')
#
#
# f1(a)

# a = 1
#
#
# def f1():
#     global a
#     a += 1
#     print(a)
#
#
# f1()
# print(a)


# def f2():
#     a = 1
#
#     def f3():
#         nonlocal a
#         a += 1
#         print(a)
#     f3()
#     print(a)
#
#
# f2()
# #
# def f(name, age=18, *hobby, **others):
#     print(f'my name is {name},i am {age} years old,i like {hobby},others {others}')
#
#
# f('jialing', 45, 'playing basketball', 'watching movie', 'playing game', other1='dsas', other2='sdfsf')

# def f():
#     return

# return True
# return [1, 2, 3]
# return (1, 2, 3, 1+2)
# return {1,3,4,1,4,45}
# return {'a':2,2:3}
# return range(10)


# print(f(), type(f()))

# def sums(a, b=0):
#     for i in a:
#         b += i
#     print(b)
#
#
# sums(b=10, a=[1, 2, 3])
#
# a = lambda x, y: x + y
# print(a(1, 2))

# def f1(x):
# #     if x % 2 == 0:
# #         return x
# #
# #
# # a = filter(f1, (1, 2, 3, 4, 0))
# #
# # print(a, type(a), list(a))

# def f2(x, y):
#     return x + y
#
#
# b = map(f2, (1, 2, 3), [4, 5, 6, 7])
# print(b, type(b), list(b))
# from functools import reduce


# def f3(x, y):
#     return x * y
#
#
# c = reduce(f3, [1, 2, 3, 4, 5], 10)
#
# print(c)

# d1 = {'a': 1, 'b': 2}
#
# del d1

# class Person:
#     name = 'jialing'
#     sex = 'male'
#     age = 22
#
#     def eat(self, *food):
#         print(f'I can eat {food}')
#
#     def say(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         print('i am %s,%s,i am %d years old' % (self.name, self.sex, self.age))
#
#
# p1 = Person()
# p2 = Person()
# print(p1.name)
# print(p1.sex)
# print(p1.age)
# p1.eat('fish', 'chicken', 'pork', 'beef')
# print(type(p1))
# p1.say('yyy', 'female', 23)
# p2.say('eee', 'male', 24)
# print(p1.__dict__)
# print(p2.__dict__)
# print(p2.name)
# print(Person.name)
# # print(Person.__dict__)
# p1.name = 'rrr'
# print(p1.name)
# print(p1.__dict__)
# Person.name = 'jiahao'
# print(Person.name)
# print(Person.__dict__)

# class Animal:
#     def __init__(self,name, sex):
#         self.name = name
#         self.sex = sex
#
#     def intro(self):
#         print(f'name:{self.name},sex:{self.sex}')
#
#
# Animal('ddd', 'male').intro()
# a1 = Animal('aaa', 'female')
# a1.intro()
# print(a1.name)

# class Teacher:
#     __name = 'jialing'
#     _sex = 'male'
#
#     def __aaa(self):
#         print('haha')
#
#     def bbb(self):
#         Teacher().__aaa()
#
#     def _ccc(self):
#         print('qqq')
#
#
# t1 = Teacher()
# print(t1._Teacher__name)
# t1._Teacher__name = 'jiahao'
# print(t1._Teacher__name)
# print(t1._sex)
# t1.bbb()
# t1._ccc()

# class Person:
#     pass
#
#
# class Student(Person):
#     name = 'jialing'
#
#
# class Teacher(Person):
#     pass
#
#
# class Infor(Teacher, Student):
#     pass
#
#
# s1 = Student()
# t1 = Teacher()
#
# print(issubclass(Student, (Person,)))
# print(issubclass(Infor, (Person, Student)))
# print(isinstance(s1, Student))
# print(isinstance(s1, Teacher))
# print(type(s1))
# print(hasattr(s1, 'name'))
# print(getattr(s1, 'name'))
# print(setattr(s1, 'name', 'jihao'))
# print(getattr(s1, 'name'))
# delattr(s1, 'name')
# print(getattr(s1, 'name'))

# f = open('1.txt', 'a')
# print(f.read())
# print(f.read(2))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# print(f.tell())
# f.seek(3, 0)
# print(f.readlines())
# f.write('ddd')
# f.write('eee')
# f.write('fff')
# f.writelines(['1\n','2\n','3'])
# print(f.name, f.mode, f.closed)
# f.close()
# print(f.closed)

# with open('1.txt', 'a') as f:
#     f.write('xxxx')

# import pickle
#
# with open('1.txt', 'rb') as f:
#     # pickle.dump('aaa', f)
#     print(pickle.load(f))
# import os

# print(os.getcwd())
# print(os.getpid())
# print(os.listdir())
# print(os.mkdir('2.txt'))
# print(os.system('cmd'))
# print(os.name)
# print(os.sep)
# print(os.curdir)
# print(os.pardir)

# import random
#
# print(random.random())
# print(random.randint(0, 7))
# print(random.randrange(1, 15, 2))
# print(random.choice('a'))

# import time
#
# print(time.time())
# print(time.localtime())
# # print(time.mktime())
# print(time.clock())
# print(time.timezone)

# try:
#     # a = 1 / 2
#     print(a)
# except NameError as t1:
#     print(t1)
# finally:
#     print('haha')

# import threading
# import time
#
# def play_game(name,count):
#     for i in range(count):
#         print(f'玩游戏{name}第{i+1}次,当前线程为{threading.currentThread()}')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#
#     t1 = threading.Thread(target=play_game, args=('NBA2k17', 10), name='t1')
#
#     t1.start()
#
#     now_time = time.time()
#
#     print(now_time)


# d1 = {k: v for k, v in ['12', '34', range(2), 'kv', [1, 2]]}
# print(d1)

# import copy
#
# a = [1, 2, 3, [2, 3]]
# b = copy.deepcopy(a)
# c = a.copy()
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))
# a[3][0] = 1
# print(a)
# print(b)
# print(c)


