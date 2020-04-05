

# 读取
f = open('1.txt','r',encoding='utf-8')

# 读
# rst1 = f.read()
# # print(rst1)

#
# rst1 = f.read(2)
# print(rst1) # 12
# rst2 = f.read(14)
# print(rst2) # 34567890123456
# rst3 = f.read(1)
# print(rst3)


#
# rst = f.readline()
# print(rst)
# rst = f.readline()
# print(rst)


# readlines()
# print(f.readlines())


#
# print(f.tell()) # 0
# f.read(1)
# print(f.tell())
# f.read(4)
# print(f.tell())
# print(f.read(12))
# print(f.tell())


# seek
print(f.tell()) # 0
# offset 偏移量
f.seek(10,0) # 文件指针开始位置0
print(f.tell()) # 10
print(f.read())
