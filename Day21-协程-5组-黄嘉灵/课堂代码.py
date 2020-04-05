# 批量创建进程
# import multiprocessing,time,os
#
# def movie(name):
#     for i in range(10):
#         print(f'看电影{name},第{i}次，当前进程id为{os.getpid()}')
#         time.sleep(0.01)
#
#
# if __name__ == '__main__':
#
#     print(f'当前时间为{time.time()},当前进程为{os.getpid()}')
#
#     pool = multiprocessing.Pool(5)
#
#     for i in range(10):
#         pool.apply_async(func=movie, args=('无间道',))
#
#     pool.close()
#
#     pool.join()
#
#     print(f'当前时间为{time.time()},当前进程为{os.getpid()}')


# #多进程下通信queue
# import multiprocessing
# import os,time
#
# def put_fn():
#     l=[1,2,3,4,5,6]
#     for i in l:
#         q.put(i)
#         print(f'当前存入queue当中{i},{os.getpid()}')
#         time.sleep(0.5)
#
# def get_fn():
#     while True:
#         if q.empty():
#             break
#         val=q.get()
#         print(f'从queue当中取{val},{os.getpid()}')
#
# if __name__ == '__main__':
#
#     print(f'当前进程为{os.getpid()},时间为{time.time()}')
#
#     q=multiprocessing.Queue()
#
#     p1=multiprocessing.Process(target=put_fn(),args=(q,))
#     p2 = multiprocessing.Process(target=get_fn(), args=(q,))
#
#     p1.start()
#     p2.start()
#
#     # p2.terminate()
#     print(f'当前进程为{os.getpid()},时间为{time.time()}')

# 多进程管道pipe
# import multiprocessing,os,time
# def send_fn(p):
#     l=[1,2,3,4,5,6]
#     for i in l:
#         p[l].send(i)
#         print(f'当前存入queue中{i},当前进程为{os.getpid()}')
#         time.sleep(0.5)
#
# def recv_fn(p):
#     while True:
#         val=p[0].recv()
#         print(f'从queue中取{val},当前进程为{os.getpid()}')
#
#
# if __name__=='__main__':
#
#     print(f'当前进程为{os.getpid()},当前时间为{time.time()}')
#
#     p=multiprocessing.Pipe()
#
#     p1=multiprocessing.Process(target=send_fn,args=(p,))
#     p2 = multiprocessing.Process(target=recv_fn, args=(p,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#
#     print(f'当前进程为{os.getpid()},当前时间为{time.time()}')

# queue.Queue
# import queue
# import threading,time
#
# def put_fn(name,q):
#     count=1
#     while True:
#         q.put(count)
#         print(f'{name}生产出来了第{count}辆大奔，当前线程{threading.currentThread()}')
#         count+=1
#         time.sleep(1)
#
# def get_fn(name,q):
#     while True:
#         val=q.get()
#         print(f'{name}购买了第{val}辆大奔，当前线程{threading.currentThread()}')
#         time.sleep(1)
#
# if __name__=='__main__':
#
#     print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
#
#     q=queue.Queue(4)
#
#     t1=threading.Thread(target=put_fn,args=('孙总',q))
#     t2 = threading.Thread(target=put_fn, args=('肖总', q))
#     t3=threading.Thread(target=get_fn,args=('李老板',q))
#     t4 = threading.Thread(target=get_fn, args=('鑫总', q))
#
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()
#
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()
#
#     print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')

# 迭代器对象
# l=[1,2,3,4]
# i1=iter(l)
# # for i in i1:
# #     print(i)
# print(next(i1))
# print(next(i1))
# print(next(i1))
# print(next(i1))


# 生成器对象
# 方式一
# g1=(i for i in range(5))   #推导式
# # for i in g1:
# #     print(i)
#
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))


# 方式二
# def fun():
#     print(1, '42行')
#     a = yield
#     print(2,a, '44行')
#     b = yield 20
#     print(3,b, '46行')
#     yield 30
#
# g = fun()
# next(g)
# g.send('jialing')
# g.send(('xiaofeng'))
# print(next(g))
# print(next(g))

# 协程生产者与消费者模型
# def consumer():
#     r=''
#     while True:
#         n=yield r
#         if not n:
#             return
#         print('consumer消费了%s'%n)
#         r='OK'
#
# def producer(c):
#     c.send(None)
#     n=0
#     while n<5:
#         n+=1
#         print('producer生产了%s'%n)
#         r=c.send(n)
#         print('consumer返回了%s'%r)
#     c.close()
#
#
# c=consumer()
# producer(c)

# 特殊赋值
# a,b='12'
# a,b=[1,2]
# a,b=(1,2)
# a,b={1,2}
# a,b={1:2,3:4}
# a,b=range(2)
# a,b=[[1,2],[3,4]]
# a,b='a','ab'
# a,b={2,2,1}
# # a,*b,c='sdfs'
# print(a,b)
