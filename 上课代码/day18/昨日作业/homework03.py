
#
f = input('请输入文件名')

file = open(f,'r',encoding='utf-8-sig')

n = input('请输入行数')

print('文件的{}前{}行内容如下'.format(f,n))

# l = file.readlines() # 所有数据 指针全部 读取

# for i in range(int(n)): # range(0,10)  0-9 10个
#     print(l[i],end=' ')
#



#
# for i in range(int(n)):
#     print(file.readline())





# readline()  readlines()

# print(file.readlines(10))

# readline(size) 指定读取某一行的size大小，如果size超出总大小，则只能读取该行。
# print(file.readline(100)) # 指定数量单位  、 换行符

# readlines(hint) hint：指定读取的size大小，但是不是行数，跟官方文档背离。
# 如果hint不够一行，则读取单位以行为标准
print(file.readlines(100))  # 指定读取大小 size 不是行数







