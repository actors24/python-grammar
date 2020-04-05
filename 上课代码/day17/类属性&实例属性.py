
class Team:
    l = [] # 类属性  [10,20]

    def add(self,value):
        self.l.append(value)
    def get_list(self):
        print(self.l)
#
t1 = Team()
t1.add(10)
t1.add(20)
t1.get_list()

# #
t2 = Team()
t2.add(30)
t2.get_list() # [10, 20, 30]


#
class A:
    name = '123'
    def set_name(self,value):
        self.name = value  # 修改 设置
    def get_name(self):
        print(self.name)

a = A()
a.get_name() # 123
a.set_name(456)
a.get_name()
