
# l = [10,20,30,40]
#
# # print() # iterator object
#
# i1 = iter(l)
#
# # for i in i1:
# #     print(i)
#
# #
# print(next(i1))
# print(next(i1))
# print(next(i1))
# print(next(i1))
# print(next(i1))


# generator object 生成器对象  for循环 可迭代对象
g1 = (i for i in range(5))  # 推导式

# print(type(g1)) # generator

# for i in g1:
#     print(i)

print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
