
import os.path as a

# 1.basename() base基本的 基础的
# print(a.basename(r'F:\python193\代码+笔记\day18\1.txt'))
# 1.txt

# 2.dirname() dir-directory目录 名字
# print(a.dirname(r'F:\python193\代码+笔记\day18\1.txt'))
# F:\python193\代码+笔记\day18

# 3.split() 分隔路径形成一个元组 元素-路径字符串，文件名字字符串
# print(a.split(r'F:\python193\代码+笔记\day18\1.txt'))
# ('F:\\python193\\代码+笔记\\day18', '1.txt')

# 4.splitext()
# 分隔路径形成一个元组 元素-路径+名字字符串，文件扩展名字符串
# print(a.splitext(r'F:\python193\代码+笔记\day18\1.txt'))
# ('F:\\python193\\代码+笔记\\day18\\1', '.txt')

# 5.join() 拼接
# print(a.join('a','b')) # a\b
# print(a.join(r'F:\python193\代码+笔记\day18','b')) # F:\python193\代码+笔记\day18\b

# 6.getsize()
# print(a.getsize('1.txt')) # 16

# 7.exists() 判断某个文件是否路径
# print(a.exists('111.txt')) # True

# 8.isabs() abs- absoulte 绝对路径
# print(a.isabs('1.txt'))
# print(a.isabs(r'F:\python193\代码+笔记\day18\1.txt'))

# 9.isdir() 目录
# print(a.isdir(r'F:\python193\代码+笔记\day18\1.txt'))
# print(a.isdir(r'F:\python193\代码+笔记\day18'))
#

# 10.isfile()
# print(a.isfile(r'F:\python193\代码+笔记\day18'))
# print(a.isfile(r'F:\python193\代码+笔记\day18\1.txt'))

# 11.ismount() 判断是否为 挂载点 盘符 C D E F
# print(a.ismount(r'F:\python193\代码+笔记\day18'))
# print(a.ismount(r'F:\\')) # True  / :linux

# 12.samefile()
# print(a.samefile(r'F:\python193\代码+笔记\day18\2.txt',r"F:\python193\代码+笔记\day18\3.txt")) # False
# print(a.samefile(r'F:\python193\代码+笔记\day18\2.txt',r"F:\python193\代码+笔记\day18\abc\2.txt")) # False
# print(a.samefile(r'F:\python193\代码+笔记\day18\2.txt',r"F:\python193\代码+笔记\day18\2.txt")) # False
# print(a.samefile(r'F:\python193\代码+笔记\day18\2.txt',r"F:\python193\代码+笔记\day18\2.txt")) # False


# 内置模块 random()
import random
#
# random.random()
# random.randint()
# random.randrange()
# random.choice()


import testmodule
testmodule.app
from testmodule import app

