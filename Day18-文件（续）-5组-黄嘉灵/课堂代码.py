# import os
# 1.getcwd() current working directory当前工作目录
# print(os.getcwd())    #D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵

# 2.listdir(url) url-path:表示路径
# print(os.listdir(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵'))   # ['1.txt', '__init__.py', '课堂代码.py']
# listdir(url):url:某一个目录路径  返回值：当前url目录下的所有内容构成一个列表

# 3.remove(url)
# 删除当前文件
# os.remove(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\1.txt')

# 4.mkdir()
# os.mkdir('1')  #在当前文件路径下创建一个目录

# 5.rmdir()
# os.rmdir('1')  #删除空目录，只能删除一层

# 6.makedirs()
# os.makedirs(r'tset1\test3')   #创建多层目录

# 7.remoovedirs()
# os.removedirs(r'test1\test2')   #删除多层空目录

# 8.rename(old,new)
# os.rename('test1','test2')  #重命名

# 9.system()
# os.system('cmd')  #进入黑窗口模式

# 10.name
# print(os.name)   #nt   windows操作系统的名字

# 11.sep  seperator-分隔符
# print(os.sep)  #操作系统的分隔符

# 12.linesep
# print(os.linesep)  # '\r\n':windows   linux:\n

# 13.curdir()
# print(os.curdir)  # . 表示当前目录

# 14.pardir()
# print(os.pardir)
# print(os.listdir('..'))  # .. 表示上一级目录

# import os.path as a
# 1.basename()
# print(a.basename(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\课堂代码.py'))   # 课堂代码.py

# 2.dirname()
# print(a.dirname(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\课堂代码.py'))    # D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵

# 3.spilt()  分割路径形成一个元组
# print(a.split(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\课堂代码.py'))   # ('D:\\PycharmProjects\\untitled\\com\\baizhi\\Day18-文件（续）-5组-黄嘉灵', '课堂代码.py')

# 4.splitext() 分割路径形成一个元组  元素-路径+名字字符串，文件扩展名字符串
# print(a.splitext(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\课堂代码.py'))

# 5.join()  路径拼接
# print(a.join(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\课堂代码.py',r'b')) # D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\课堂代码.py\b

# 6.getsize()
# print(a.getsize('1.txt'))  # 7

# 7.exists()  判断某个文件是否存在
# print(a.exists(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\1.txt'))  # True

# 8.isabs()   是否是绝对路径
# print(a.isabs(r'1.txt')) #False

# 9.isdir() 判断是否是目录
# print(a.isdir(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵'))  #True

# 10.isfile()  判断是否是文件
# print(a.isfile(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\1.txt')) # True

# 11.ismount()  判断是否为 挂载点 盘符  C D E F
# print(a.ismount(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\1.txt'))  #False
# print(a.ismount(r'F:\\'))  #True

# 12.samefile()
# print(a.samefile(r'D:\PycharmProjects\untitled\com\baizhi\Day18-文件（续）-5组-黄嘉灵\1.txt',r'D:\PycharmProjects\untitled\com\baizhi\hjl\1.txt'))  # True


# import random
#
# random.random()
# random.randint()
# random.randrange()
# random.choice()

# 异常
# # 异常处理
# try:
#     f = open('1.txt')
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print('你输入的文件路径有误，请重新输入')
#
# try:
#     a = 10
#     b = 20
#     print(a + b)
# except ValueError:
#     print('在干嘛呢')
#
# print(123)

# try:
#     a=10
#     b=20
#     print(a+b1)
#     print(100)
# except  NameError:
#     print('在干嘛呢')
#
# print(123)

# try:
#     a=10
#     b=20
#     print(a+b1)
#     print(100)
# except ValueError as tips:
#     print(tips)
#     print('在干嘛呢')
#
# print(123)

# try:
#     a=10
#     b=20
#     print(a+b1)
#     print(100)
# except ValueError as tips1:
#     print(tips1)
#     print('在干嘛呢')
# except NameError as tips2:
#     print(tips2)
#     print('在干嘛呢')
# except ImportError as tips3:
#     print(tips3)
#     print('在干嘛呢')
#
# print(123)

# try:
#     a=10
#     b=20
#     print(a+b1)
#     print(100)
# except Exception as tips1:
#     print(tips1)

# try:
#     a=10
#     b=20
#     print(a+b1)
#     print(100)
# except :
#     print('afa')
#
# print(123)

# try:
#     a=10
#     b=20
#     print(a+b1)
#     print(100)
# except :
#     print('afa')
# finally:
#     print('sdfsdfsfwec')
#
# print(123)
