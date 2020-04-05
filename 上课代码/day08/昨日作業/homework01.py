
# 1.str = "小明:87;小花:81;小红:97;小天:76;小张:74;小小:94;小西:90;小伍:76;小迪:64;小曼:76;张小四:33";
# 求所有人的平均成绩

s1 = "小明:87;小花:81;小红:97;小天:76;小张:74;小小:94;小西:90;小伍:76;小迪:64;小曼:76;张小四:33"
# split()
list1 = s1.split(';')
print(list1)
# ['小明:87', '小花:81', '小红:97', '小天:76', '小张:74', '小小:94', '小西:90', '小伍:76', '小迪:64', '小曼:76', '张小四:33']
# 兩個方案
# 方案一
# sums = 0
# for i in list1:
#     # print(i) # 小串 '小明:87'
#     new_list = i.split(':')
#     print(new_list[1])
#     sums += int(new_list[1])
# print(sums / len(list1))

# 方案二：
# sums = 0
# for i in list1:
#     print(i)
#     index = i.index(':')
#     print(index)
# #     切片 數字
#     print(i[index+1:])
#     sums += int(i[index+1:])
# print(sums / len(list1))
