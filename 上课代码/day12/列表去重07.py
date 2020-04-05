# 列表
# 列表中 元素 进行 去重 - 去掉重复
list1 = [10,20,30,40,10,20,30,40]
print(list(set(list1))) # {40, 10, 20, 30} [40, 10, 20, 30]

# 通过程序来实现 去重
# 空列表
new_list = []
for i in list1:
    if i not in new_list:
        new_list.append(i) # 10 20 30 40
print(new_list)