

student_list = [
    ['李伟东','193班',507,'python班级'],
    ['张三','190班',506,'java班级'],
    ['王老师','508办公室',508,'办公室'],
]

# 实现 人员信息 逐一介绍

# print()
# for l in student_list:
#     print(l[0],l[1],l[2],l[3])


# 面向对象编程
# 人 对象
# 类
# name 班号  房间号 note
# 介绍  print()
class Member:
    # 属性 方法
    def __init__(self,name,classnum,roomnum,note):
        self.name = name
        self.classnum = classnum
        self.roomnum = roomnum
        self.note = note
    # 方法
    def intro(self):
        print(self.name,self.classnum,self.roomnum,self.note)

mem1= Member('李老板','193班',507,'python班级')
mem1.intro()

