
import threading
import time
# 函数

def movie(name):
    for i in range(20):
        print(f'看电影{name},第{i}次,当前线程{threading.currentThread()}')
        time.sleep(0.1)


def music(name,count):
    for i in range(count):
        print(f'听歌{name},第{i}次,当前线程{threading.currentThread()}')
        time.sleep(0.2)


if __name__ == '__main__':
    print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
    # 创建线程对象
    t1 = threading.Thread(target=movie,args=('python193',))
    t2 = threading.Thread(target=music,args=('今天是个好日子',20), daemon=True)

    t1.setName('t1')
    t2.setName('t2')
    # t2.setDaemon(True)
    # t1.setDaemon(True)
    t1.start()
    t2.start()
    # 常用方法属性
    # t1.join()
    # t2.join()
    # setDaemon()
    # print(t1.isAlive()) # False
    # print(t2.isAlive()) # True

    # 常用属性
    print(t1.name) # t1
    print(t1.ident) # identify id 5600
    print(t2.daemon) #
    print(t2.isDaemon()) #

    print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')

    # print(t2.is_alive())
    # print(t2.isAlive()) # True