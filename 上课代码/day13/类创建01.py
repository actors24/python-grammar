
# 人类 内容
# 属性：名字 性别 年龄
# 方法：吃喝 睡 走
class Person:
    # 三个属性
    name = '李老板'
    age = 100
    sex = '女'
#     方法
    def eat(self,food):
        print(f'吃{food}')

#创建对象
p1 = Person()  # 实例 实例对象 对象   instance-实例   isinstance()
# print(p1)
# print(type(p1))
p2 = Person()
# print(p2)
p3 = Person()
p4 = Person()

# 访问 操作 属性 方法
# 访问属性 点语法
# print(p1.name) # 李老板
# print(p1.age) # 99
# print(p1.sex) # 女
#
# # 方法访问 点语法
# p1.eat('jiaozi')

# p2对象 访问
# print(p2.name)
# print(p2.age)
# print(p2.sex)



# 查看 p1 对象 所有成员
print(p1.__dict__) # {}
print(p1.age)
print(p2.age)
print(p3.age)




# l1 = list('123')  ['1','2','3']
# l1 = list(range(5))  [0,1,2,3,4]
# l1.reverse() l1.sort()  remove()


# 字典 集合 常用方法
# dict1 = {'name':'123','age':18}
# dict1 = dict()  # list() tuple() str()
# print(dict1)
# print(type(dict1))