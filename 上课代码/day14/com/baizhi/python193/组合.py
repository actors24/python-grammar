# class B:
#     hehe=100
#
# class A:
#     age=18
#     age=int()  # 属性名=类（）
#     b=B()  # b:是B的实例对象 是A的类属性
#
#
#
# # int:是个类
#
# a=A() # 创建A的实例对象
#
# print(a.age)  # age：是int的实例对象，底层修改了打印方法，不直接显示对象，而是显示数值
# print(a.b)  # b:是一个实例对象
# print(a.b.hehe)
#
#
# # 所有的类中的属性，都是：   属性名=类()




class Teacher:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# 1. 类属性  组合
# class School:
#     teacher=Teacher('xiaobo',40)
#     student=Student('jiangang',18)

# 2. 实例属性  组合

# class School:
#     def kai_xue(self):
#         self.teacher=Teacher('xiaobo',40)
#         self.student=Student('jiangang',18)
#
# # 3. 实例属性  组合
#
# class School:
#     def kai_xue(self,t_name,t_age,s_name,s_age):
#         self.teacher=Teacher(t_name,t_age)
#         self.student=Student(s_name,s_age)
#
# # # 3. 实例属性  组合
#
# class School:
#     def __init__(self,t_name,t_age,s_name,s_age):
#         self.teacher=Teacher(t_name,t_age)
#         self.student=Student(s_name,s_age)


# # 3. 实例属性  组合

class School:
    def __init__(self,teacher,student):
        self.teacher=teacher
        self.student=student

school=School(Teacher('xiaobo',40),Student('jiangang',18))
# school.kai_xue('xiaobo',40,'jiangang',18)
print(school.teacher.name)
print(school.student.name)

# print(school.teacher.name)
# print(school.student.name)















