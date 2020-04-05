
# 1.add()
# set1 = {10,20,30}
# # rst = set1.add(40)
# rst = set1.add(30)
# print(rst) # None
# print(set1) # {40, 10, 20, 30}

# 2.clear()
# set1 = {10,20,30}
# print(set1.clear()) # None
# print(set1) # set()

# 3.discard()
# set1 = {10,20,30}
# # print(set1.discard(100)) # None
# # print(set1) # {20, 30}

# pop()
# set1 = {'123',67,20,30,True,None}
# print(set1.pop()) # 10
# print(set1)

# remove()
# set1 = {'123',67,20,30,True,None}
# print(set1.remove(300)) # None
# print(set1)

# update()
# set1 = {'123',67,20,30,True,None}
# # print(set1.update({10,20})) # None
# # print(set1.update({10,20},{30,40,50})) # None
# # print(set1.update()) # None
# print(set1) #


# difference()
# set1 = {'123',67,20,30,True,None}
# print(set1.difference({10,20,30})) # {True, 67, None, '123'}
# print({10,20,30}.difference(set1)) # {10}
# print({10,20,30}.difference(set1,{40,50,60,10})) # set()
# print(set1)

# difference_update()
# set1 = {'123',67,20,30,True,None}
# print(set1.difference_update({10,20,30})) # None
# print(set1) # {True, 67, '123', None}

# intersection()
# intersection_update()

# symmetric_difference()
# symmetric_difference_update()

# isdisjoint(...)

# union()