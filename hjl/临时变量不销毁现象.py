def fun():
    l=[]
    for i in range(3):       #i不销毁（内存泄漏问题）
        def fun2(x):
            print(x+i)
        l.append(fun2)
        return 1
for i in fun():
    l(2)