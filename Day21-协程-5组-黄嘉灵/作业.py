# #1.
# import threading
#
# n=0
# def fn1():
#     info = [1, 2, 3, 4, 55, 233]
#     global n
#     print(f'当前值为{info[n]},线程号为{threading.currentThread()}')
#     n += 1
#
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=fn1, args=())
#     t2 = threading.Thread(target=fn1, args=())
#     t3 = threading.Thread(target=fn1, args=())
#     t4 = threading.Thread(target=fn1, args=())
#     t5 = threading.Thread(target=fn1, args=())
#     t6 = threading.Thread(target=fn1, args=())
#
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#     t5.start()
#     t6.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#     t5.join()
#     t6.join()
#
#     print('the end')


# 2.
# def fn2(n):
#     l1 = []
#     l1.append(0)
#     l1.append(1)
#     for i in range(2, n):
#         l1.append(l1[-1]+l1[-2])
#     for j in range(n):
#         yield l1[j]
#
#
# g = fn2(10)
# for j in range(10):
#     print(next(g))

# 3.
# def fn3():
#     print()
#     while 1:
#         x = yield
#         print(f'x={x}')
#         print(f'x={x}')
#
#
# g = fn3()
# next(g)
# g.send('haha')

# 4.
import threading
import time

sum_money = 500


def fn4():
    money = 0
    n = 1
    global sum_money
    while 1:
        money += 1
        sum_money += 1
        print(f'当前刷卡{threading.currentThread().name}已经刷了{n}次,刷卡机已有{money}元,总账户已有{sum_money}元')
        n += 1
        time.sleep(1)
        if money == 100:
            break


if __name__ == '__main__':
    t1 = threading.Thread(target=fn4, args=(), name='1号机')

    t2 = threading.Thread(target=fn4, args=(), name='2号机')
    t3 = threading.Thread(target=fn4, args=(), name='3号机')
    t4 = threading.Thread(target=fn4, args=(), name='4号机')
    t5 = threading.Thread(target=fn4, args=(), name='5号机')
    t6 = threading.Thread(target=fn4, args=(), name='6号机')
    t7 = threading.Thread(target=fn4, args=(), name='7号机')
    t8 = threading.Thread(target=fn4, args=(), name='8号机')
    t9 = threading.Thread(target=fn4, args=(), name='9号机')
    t10 = threading.Thread(target=fn4, args=(), name='10号机')

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
