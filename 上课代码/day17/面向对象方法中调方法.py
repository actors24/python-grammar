

class A:
    name = 'abc'
    def fn1(self):
        print('我是fn1','6hang')
        B.fn2(self)

    # def fn2(self):
    #     print('我是fn2','9行')
    #     print(self.name,'10行')
    #     # self.fn1()


a = A()
a.fn1()

class B:
    def fn2(self):
        print('我是fn2','9行')

        # self.fn1()



# a = A()
# # a.fn2()
# # a.fn1()
# a.fn1()




# a = A()
# a.fn2()
# a.fn1()
#
# b = A()