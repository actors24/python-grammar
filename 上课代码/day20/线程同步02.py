import threading
import time

# 锁
lock = threading.RLock() # 可重入锁
class MyList:
    def __init__(self):
        self.l = ['A','B','','']
        self.index = 2

    def add_member(self,value):
        print(threading.currentThread(),'12行')
        lock.acquire() # 获取 获得 申请锁
        print(threading.currentThread(),'14行')
        lock.acquire() # 获取 获得 申请锁
        self.l[self.index] = value  # l[2]='c'  [a,b,C] L[3] = 'd'
        print(threading.currentThread(),'17行')
        time.sleep(1)
        self.index += 1  # index: 3
        print(threading.currentThread(), '20行')
        lock.release() # 释放 锁
        print(threading.currentThread(), '22行')

        lock.release() # 释放 锁

    def get_list(self):
        return self.l

if __name__ == '__main__':


    print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')

    # MyList创建对象
    mylist = MyList()
    # mylist.add_member()
    # 创建线程对象
    t1 = threading.Thread(target=mylist.add_member,args=('C',),name='t1')
    t2 = threading.Thread(target=mylist.add_member,args=('D',),name='t2')

    t1.start()
    t2.start()

    t2.join()
    t1.join()



    print(mylist.get_list())


    print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
