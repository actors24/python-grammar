
# sorted()

def fn1(fn):
    print(fn,id(fn))
    fn()

# 参数 - 函数
def fn2():
    print('蒋浩楠是充话费送的！')
#     fn2 代表 名为fn2的函数体
fn1(fn2)

print(fn2,id(fn2))
# print(fn2)
# a = 10
# print(a)