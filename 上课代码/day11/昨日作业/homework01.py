
def fn1():
    a = 10
    return 10,True,[10,20,30]

print(fn1())


def fun(x,y,a,b):
    return x*y+a*b
#
# def fun(l1,l2):
#     print(l1,l2)
#
# fun([10,20,30],[40,50])

# def outside():
#     print('outside!')
#     def inside():
#         print('inside!')
#     inside()


def outside():
    var = 5
    def inside():
        nonlocal var
        print(var) # 5
        var = 3
        print(var)  # 3
    inside()
    print(var) # 3
outside()

# def fun_A(x, y=3):
# return x * y
print((lambda x,y=3: x * y)(10,10))

# lambda x : x if x % 2 else None
def fn(x):
    if x % 2 == 0:
        return None
    else:
        return x
print(fn(10))

#
def fn2(num):
#     输出这个整数的所有因子
    for i in range(1,num + 1):
        if num % i == 0:
            print(i)

fn2(10)

#
def fn3(num):
    print('hello world' * num)

# num = int(input('请输入一个整数'))
# fn3(num)

# 输出整数 位数
# def fn4(num):
# #     print(len(num))
# # s1 = input('请输入一个整数')
# # fn4(s1)


def fn4(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count
# s1 = int(input('请输入一个整数'))
# print(fn4(s1))


count = 0  #
def fn5(num):  # 123  12
    if num == 0:
        return
    global count
    num //= 10  #  num:12  1  0
    count += 1  # count:1  2 3
    fn5(num)  # fn5(12) fn5(1) fn5(0)

fn5(123)

print(count)


