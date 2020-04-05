# import threading
# import time
#
# def movie(name):
#     for i in range(10):
#         print(f'看电影{name},第{i}次，当前线程{threading.currentThread()}')
#         time.sleep(0.4)
#
# def music(name,count):
#     for i in range(count):
#         print(f'听歌{name},第{i}次,当前线程{threading.currentThread()}')
#         time.sleep(0.2)
#
# if __name__=='__main__':
#     print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
#     #创建线程对象
#     t1=threading.Thread(target=movie,args=('在哪呢',))
#     t2=threading.Thread(target=music,args=('七里香',10))
#
#     t1.setName('t1')
#     t2.setName('t2')
#     t1.setDaemon(True)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(t1.isAlive())
#     print(t2.isAlive())
#     print(t1.name)
#     print(t2.name)
#     print(t1.daemon)
#     print(t2.daemon)
#
#     print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
#     print(t1.isAlive())
#     print(t2.isAlive())

# 线程同步
# import threading
# import time
#
# lock = threading.RLock()
#
#
# class MyList:
#     def __init__(self):
#         self.l = ['A', 'B', '', '']
#         self.index = 2
#
#     def add_member(self, value):
#         print(threading.currentThread(), '48行')
#         lock.acquire()
#         print(threading.currentThread(), '50行')
#         lock.acquire()
#         self.l[self.index] = value
#         print(threading.currentThread(), '53行')
#         time.sleep(1)
#         self.index += 1
#         print(threading.currentThread(), '56行')
#         lock.release()
#         print(threading.currentThread(), '58行')
#         lock.release()
#
#     def get_list(self):
#         return self.l
#
#
# if __name__ == '__main__':
#     print(f'当前线程为{threading.currentThread()}，当前时间为{time.time()}')
#
#     mylist = MyList()
#     t1 = threading.Thread(target=mylist.add_member, args=('C',), name='t1')
#     t2 = threading.Thread(target=mylist.add_member, args=('D',), name='t2')
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print(mylist.get_list())
#
#     print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')

# 多进程
# import multiprocessing
# import os
# import time
#
#
# def movie(name):
#     for i in range(10):
#         print(f'看电影{name},第{i}次，当前进程为{os.getpid()}')
#
#
# def music(name,count):
#     for i in range(count):
#         print(f'听歌{name},第{i}次，当前进程为{os.getpid()}')
#         # time.sleep(0.2)
#
#
# if __name__=='__main__':
#
#     print(f'当前进程为{os.getpid()},当前时间为{time.time()}')
#     p1=multiprocessing.Process(target=movie,args=('我和我的祖国',))
#     p2=multiprocessing.Process(target=music,args=('七里香',10))
#
#     p1.start()
#     p2.start()
#
#     print(f'当前进程为{os.getpid()},当前时间为{time.time()}')

# 进程池
# import multiprocessing
# import os
#
#
# def movie(name):
#     for i in range(5):
#         print(f'看电影{name},第{i}次，当前进程为{os.getpid()}')
#         # time.sleep(0.1)
#
#
# if __name__ == '__main__':
#
#     pool = multiprocessing.Pool(2)
#
#     for i in range(5):
#         pool.apply_async(func=movie, args=('我和我的祖国',))
#
#     pool.close()
#
#     pool.join()
