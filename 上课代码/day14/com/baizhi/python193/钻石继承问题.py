class GrandPa(object):
    def __init__(self):
        super().__init__() # object的init
        print('我是爷爷')

class Father(GrandPa):
    def __init__(self):
        # GrandPa.__init__(self)
        super().__init__()
        print('我是爸爸')

class Uncle(GrandPa):
    def __init__(self):
        # GrandPa.__init__(self)
        super().__init__()
        print('我是叔叔')

class Son(Father,Uncle):
    def __init__(self):
        # Father.__init__(self)
        # Uncle.__init__(self)
        # super() 指代父类实例对象
        super().__init__()
        print('我是儿子')

s=Son()

# for i in Son.mro():
#     print(i)
print(Son.mro())

# print(object.__dict__)

print(GrandPa.mro())
