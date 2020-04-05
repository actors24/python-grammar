class A:pass
class B:pass
class C(A):
    age=18

# print(issubclass(C,A))
# print(issubclass(C,B))
# print(issubclass(C,(A,B)))
#
# c=C()
# print(isinstance(c,C))
# print(isinstance(c,B))
# print(isinstance(c,A))
# print(isinstance(c,(A,B)))

c=C()
print(hasattr(c,'age'))
print(hasattr(c,'sex'))
print(getattr(c,'age'))
print(getattr(c,'hehe','erro'))
setattr(c,'hehe',100)
print(getattr(c,'hehe'))
print(c.hehe)

delattr(c,'hehe')
print(c.hehe)

