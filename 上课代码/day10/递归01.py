
# RecursionError
# 递归
# def fn1():
#     print('蒋浩楠今天中午吃什么?')
#     fn1()  # 调用自己
# fn1()


# 应用场景一
# 依次打印输出 10 9 8 7 6 5 4 3 2 1

# 循环
# for i in range(10,0,-1):
#     print(i)

#
# def fn1(num):
#     if num == 0:
#         return
#     print(num)
#     num -= 1
#     fn1(num)
#
# fn1(10)


# 阶乘
# 求某个数字的阶乘
# 5*4*3*2*1
# sums = 1
# for i in range(1,6):
#     sums *= i
# print(sums)

'''
num = 5   5 * fn(4)
num=4     5 * 4 * fn(3)
num=3     5 * 4 * 3 * fn(2)
num = 2    5 * 4 *3 * 2 * fn(1)
num = 1    5 * 4 *3 *2 * 1 * fn(0)

dept 
'''

# def fn(num):
# #     乘法运算  5 * 4 * 3 * 2 * 1
#     if num == 1:
#         return 1
#     return num * fn(num-1)
#
# print(fn(5))




# 斐波那契数列
# 0 1 1 2 3 5 8 13 21 。。。。
# 从第三位开始， 第N项 是 前两位数字之和

# 循环 完成
# 函数 递归
# 第N项 数字 是几？

'''
n = 8  返回值： fn(7) +  fn(6)
               n = 7          n=6
            fn(6) + fn(5) + fn(5) + fn(4) 2
               5       3        3     fn(3) + fn(2)  
                                   fn(2) + fn(1)       +     1      
                                     1 +  0      + 1
'''

def fn(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fn(n-1) + fn(n-2)

# n = 3 第3项 数字 是 1
#  n=2 第2项 数字是 ？
#  n=1 第1项 数字是 ？

# 打印 函数fn调用的 返回值
print(fn(8))  # 1



# 汉诺塔问题