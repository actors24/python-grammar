
# print(a)
# 全局变量
a = 10


# 全局作用域 访问 全局变量
print(a)


# 声明一个函数
def fn1():
    # 局部作用域 访问 全局变量
    print(a)
#     局部变量
    b = 20
    print(b)
fn1()


# 全局作用域下 访问 b
# print(b)

