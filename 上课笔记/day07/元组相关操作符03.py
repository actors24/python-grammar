#
# t1 = (10,)
# t2 = ('hailong',18,True,'female')

# 1.+
# print(t1 + t2) # (10, 'hailong', 18, True, 'female')
# print(t1) # (10,)
# print(t2) #('hailong', 18, True, 'female')

# 2.*
# print(t1 * 3) # (10, 10, 10)
# print(t1) # (10,)

# # 3. in  not in
# print('hailong' in t2) # True
# print('hailong' not in t2) # False

# 4.比较运算符
t1 = (10,)
t2 = (18,'hailong',True,'female')
t3 = (9,10)
print(t1 > t3) # True
print(t1 > t2) # False
t4 = (18,'xinzong',False)
print(t2 > t4) # False
