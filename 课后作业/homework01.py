
# 父类
class Role(object):
    def __init__(self,name):
        self.name = name
    def attack(self):
        return None

# 子类
# Magicer
class Magicer(Role):
    base_hurt = 5
    def __init__(self,level,name):
        if level >= 1 and level <= 10:
            self.level = level
            super().__init__(name)
    def attack(self):
#         计算 伤害值  等级 * 5
        if self.level:
            return self.base_hurt * self.level

# m1 = Magicer(5,'王国强')
# print(m1.attack())

# Soldier战士
class Soldier(Role):
    def __init__(self,hurt,name):
        self.hurt = hurt
        super().__init__(name)
    def attack(self):
        return self.hurt
# s1 = Soldier(10,'胡奎')
# print(s1.attack())

# Team类  团队
class Team(object):
    def __init__(self):
        self.l = []
        # self.sum1 = 0
    def add_member(self,*member):  # 添加 成员 保存 保证 总数最多为6人
       print(len(self.l))
       if len(self.l) + len(member) >= 6:
           print('本队已满')
       else:
           self.l.extend(member)
           print('添加成功')
    def attack_sum(self):
        self.sum1 = 0
        for i in self.l:
            print(i,i.attack())
            # print()
            self.sum1 += i.attack()  # self.sum1 = self.sum1 + i.attack()
        return self.sum1

# 生成对象
team1 = Team()
# Magicer  Soldier
m1 = Magicer(5,'王国强')
m2 = Magicer(10,'王国强1')
m3 = Magicer(6,'王国强2')
s1 = Soldier(10,'胡奎')
s2 = Soldier(100,'胡奎1')
s3 = Soldier(200,'胡奎2')
s4 = Soldier(2000,'胡奎3')
# team1.add_member(m1)
# team1.add_member(s1)
# team1.add_member(s2)
# team1.add_member(s3)
# team1.add_member(s4)
# team1.add_member(m2)
# team1.add_member(m1,m2,m3)
# print(team1.l)
# team1.add_member(s1,s2)
# print(team1.l)
# team1.add_member(s3,s4)
# print(team1.l)

team1.add_member(m1,m2,m3) #
print(team1.attack_sum()) # 105
team1.add_member(s1,s2)  # 10 100
print(team1.attack_sum()) #


