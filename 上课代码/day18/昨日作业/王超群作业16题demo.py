# 1.下面只有一种方式不能打开文件，是哪一种？
# >>> f = open('E:/test.txt', 'w')  # A
# >>> f = open('E:\test.txt', 'w')  # B
# >>> f = open('E://test.txt', 'w') # C
# >>> f = open('E:\\test.txt', 'w') # D
# 答:
# B
# 原因: \t(斜杠t)表示制表符
# 使用: \\t 或 r'E:\test.txt' 进行转义 或 将斜杠 \ 改为 反斜杠 /
# 改为: f = open('E:\\test.txt', 'w') 或 f = open(r'E:\test.txt', 'w') 或 f = open(r'E:/test.txt', 'w')


# 2.打开一个文件使用open()函数，通过设置文件的打开模式，决定打开的文件具有那些性质，请问默认的打开模式是什么？
# 答:
# 默认的打开模式是: r 只读模式,文件的指针将会放在文件的开头,如果文件不存在,会抛出异常(报错)


# 7.open('E\\Test.bin','xb')是以什么样的模式打开的文件？
# 答:
# 只写模式,以二进制形式


# 9.为什么打开了文件，在不需要的时候要使用close()方法将文件对象关闭？
# 答:
# ①写入内容时,写入的内容此时是保存在缓存中的,使用close()方法将缓存中的内容保存在文件中,不使用close()方法,写入的内容将丢失
# ②关闭文件操作IO流,释放系统资源


# 10如何迭代打印出文件对象中的每一行数据？
# 答:
# f = open('静夜思.txt', 'r+', encoding='utf-8')
# # f.write('床前明月光,\n疑是地上霜,\n举头望明月,\n低头思故乡。')
# for i in f.read():
#     print(i, end='')


# 11.文件对象的内置方法read([size=1])作用是读取文件对象内容，size参数时可选的，如果设置size=10，将返回什么？
# 答:
# 读取后的内容是前10个字符


# 12.如何获得文件对象当前的指针位置？
# 答:
# 使用 tell() 方法监听指针当前位置


# 13.请将文件:hehe.mp3打印到控制台
# 答:
# import os.path as p
# print(p.basename(r'D:\PyCharm\mycode\Python_193\pythonBasics\task\Day17-文件-3组-王超群\hehe.mp3'))
# print(open('hehe.mp3', 'rb').read())


# 14.将上一题的文件保存为新文件:hehe.txt
# 答:
# import os
# os.rename('hehe.mp3', 'hehe.txt')


# 15.*编写一个程序，接收用户的输入并保存为新的文件，程序实现如图:
# 答:
import sys


def save_file():
    name = input('请输入文件名(包含后缀名):')
    print("请输入内容【单独输入':w'保存退出】")
    f = open(name, 'a', encoding='utf-8')
    while True:
        data = input()
        if data == ':w':
            f.close()
            sys.exit()
        f.write(data + '\n')


# save_file()


# 16.*编写一个程序，比较用户输入的两个文件，如果不同，
# 显示出所有不同处的行号与第一个不同字符的位置，程序实现如图:
# 答:
def check_file():
    name1 = input('请输入需要比较的头一个文件名:')
    name2 = input('请输入需要比较的另一个文件名:')
    flag = 0
    f1 = open(name1, 'r', encoding='utf-8')
    f2 = open(name2, 'r', encoding='utf-8')
    data1 = f1.readlines()
    data2 = f2.readlines()
    for i, j in zip(data1, data2):
        if i != j:
            flag += 1
            print(f'第 {flag} 行不一样')
        else:
            flag += 1


# check_file()


# 17.*编写一个程序，当用户输入文件和行数(n)后，
# 将该文件的前n行内容打印到屏幕上，程序实现如图:
# 答:
def open_file():
    name = input(r'请输入可打开的文件,如:(C:\test:record.txt):')
    num = input('请输入需要显示该文件行数范围,如(7:10):')
    l = num.split(':')
    f = open(name, 'r', encoding='utf-8')
    print(f'文件{name}的第{l[0]}到{l[1]}的内容如下:')
    data = f.readlines()[int(l[0]):int(l[1]) + 1]
    for i in data:
        print(i, end='')

# open_file()
