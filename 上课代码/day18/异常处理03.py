

# 打算 打开文件进行操作
try:
    f = open('111.txt')
    f.read()
    f.close()
except FileNotFoundError:
    print('您输入的文件路径有误，请重新输入')

a = 10
b = 20
def fn():
    print('我是fn')