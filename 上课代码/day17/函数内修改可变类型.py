#
# list1 = [10,20,30]
#
# def fn():
#     list1.append(40)
#
# fn()
# print(list1)

class A:
    l = []
    def fn1(self,value):
        self.l.append(value)


a = A()
a.fn1(10)


b = A()
b.fn1(20)

print(b.l)  # [10,20]










