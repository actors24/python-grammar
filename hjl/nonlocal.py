def fun1():
    a=100
    def fun2():
        a=200
        def fun3():
            nonlocal a
            a=300
            print(a,'fun3')
        fun3()
        print(a,'fun2')
    fun2()
    print(a,'fun1')
fun1()