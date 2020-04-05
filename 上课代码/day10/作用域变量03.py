
# 函数嵌套调用

def fn1():
    print('fn100')


def fn2():
    print('fn200')
    fn1()


# a = 5
def fn3():
    # 局部变量
    a = 10
    print(a,'17行')  # 5
    def fn4():
        print(a,'19行')  # 5
        print('fn4')
    fn4()
fn3()

# fn4()
print(a,'25行') # 5