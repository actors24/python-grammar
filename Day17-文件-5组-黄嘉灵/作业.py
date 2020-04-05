# 1.B

# 2.默认的打开方式为只读

# 7.报错

#8.用readlines方法

# 9.释放系统资源，减少内存压力

# 10.
# f=open('11.txt')
# for i in f.readlines():
#     print(i)


# 11.返回文件中的头十个字符

# 12.用tell()可以监听文件指针当前位置

# 13.
# f=open('hehe.mp3','rb')
# print(f.read())

# 14.
# f=open('hehe.mp3','rb')
# g=open('hehe.txt','w')
# rst=f.readlines()
# for i in rst:
#     g.writelines(str(i))

# 15.
# n=input('请输入文件名:')
# f=open(n,'w')
# m=input('请输入内容:【单独输入":w"保存退出】:\n')
# f.write(m)
# while 1:
#     o=input('')
#     if o!=':w':
#         f.write(o + '\n')
#     if o==':w':
#         f.close()
#         exit()

# if ':w' in f.writelines(m):
#     f.close()

# 16.
# m=input('请输入需要比较的头一个文件名:')
# n=input('请输入需要比较的另一个文件名:')
# a=open(m)
# b=open(n)
# rst1=a.readlines()
# rst2=b.readlines()
# rst=[]
# rst.extend(rst1)
# rst.extend(rst2)
# sums=0
# for i in range(len(rst)//2):
#     if rst[i]!=rst[len(rst)//2+i]:
#         print(f'第{i+1}行',end=',')
#         for j in range(len(rst[i])):
#             for k in range(len(rst[len(rst)//2+i])):
#                 if k==j:
#                     if rst[i][j]!=rst[len(rst)//2+i][k]:
#                         print(f'第{j+1}个不一样',end=',')
#         sums+=1
#         print()
# print(f'两个文件共有【{sums}】处不同')

# 17.
# m=input('请输入要打开的文件:')
# n=int(input('请输入需要显示该文件前几行'))
# a=open(m)
# rst=a.readlines()
# for i in range(n):
#     print(rst[i])

f=open('11.txt')
print(f.readlines(100))