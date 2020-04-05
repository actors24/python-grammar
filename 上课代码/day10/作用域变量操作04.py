
# 全局变量
a = 10
# local variable  UnboundLocalError
def fn1():
    # 场景一
    # a += 10
    # 场景二
    # a = a + 10
    # 场景三：
    # print(a)
    # a = 20

    # a = 10  #
    # a += 10
    # print(a,id(a)) # 20

#     使用  global
    global a
    a += 10
    print(a,id(a))

# fn1()
# print(a,id(a)) # 10


# demo

# def fn2():
#     global b
#     b = 20
#     print(b)
# fn2()
# print(b)
#
# b = 30
# print(b)


# demo2
# c = 100
# def fn3():
#     global c
#     c += 100
#     print(c) # 200
#     def fn4():
#         global c
#         c += 100
#         print(c)
#
# fn3()
# print(c)


# nonlocal
def fn5():
    d = 100
    print(d,'58行') # 100
    def fn6():
        nonlocal d
        d += 100
        print(d) # 200
        def fn7():
            nonlocal d
            d += 100
            print(d)
        fn7()
    fn6()
    print(d,'64行')  # 300
fn5()


e = 200
def fn7():
    e = 300
    def fn8():
        global e
        print(e,id(e),'78hang') # 200
        # nonlocal e
        # print(e, id(e), '82hang')  # 300
        # e += 100
        # print(e, id(e), '84hang')  # 400
    fn8()
    def fn9():
        nonlocal e
        print(e, id(e), '82hang') # 300
        e += 100
        print(e, id(e), '84hang') # 400
    fn9()
    print(e,id(e),'86Hang') # 400
fn7()
print(e,id(e)) # 200
