import os

# 1.getcwd() cwd current working directory当前工作目录
# print(os.getcwd()) # F:\python193\代码+笔记\day18

# 2.listdir(url) url-path:表示 路径  listdir directory
# print(os.listdir(r'F:\python193\代码+笔记\day18'))
# ['.idea', '1.txt', '11.txt', 'day18.md', 'os模块02.py', 'pickle01.py', '昨日作业']
# listdir(url)
# url:某一个目录路径
# 返回值：当前url目录下的所有内容构成一个列表

# 3.remove(url)
# os.remove('2.txt')

# 4.mkdir() mk-make dir-目录
# 创建 单层目录
# os.mkdir('test1')
# os.mkdir(r'F:\python193\代码+笔记\day18\test1\test1')

# 5.rmdir()  rm-remove 删除空目录
# os.rmdir('test')
# os.rmdir(r'test1')


# 6.makedirs()  创建多层目录
# os.mkdir(r'test\test1')
# os.makedirs(r'test\test1')


# 7.removedirs() 删除多层空目录
# os.removedirs(r'test1\test1')

# 8.rename() re-重新
# os.rename('2.txt','3.txt')
# os.rename(r'F:\python193\代码+笔记\day18\3.txt',r'F:\python193\代码+笔记\day18\4.txt')
# os.rename(r'F:\python193\代码+笔记\day18\4.txt','5.txt')

# 9.system()
# os.system('cmd')


# 10.name
# print(os.name)  # nt  Microsoft windows new techonoly

# 11. sep   路径分隔符 seperator-分隔符
# print(os.sep) # \ windows  linux：/

# 12.linesep
# print(os.linesep) # '\r\n' :windows  linux:\n

# 13.curdir cur-current 当前目录
# print(os.curdir) # .
# print(os.listdir('.'))

# 14.pardir par-parent 上一级目录
# print(os.pardir) # ..
