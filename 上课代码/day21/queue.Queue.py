import queue
import threading, time


# 发送数据
def put_fn(name, q):
    count = 1
    while True:
        q.put(count)
        print(f'{name}生产出来了第{count}辆大奔,当前线程{threading.currentThread()}')
        count += 1
        # time.sleep(1)


# 发送数据
def get_fn(name, q):
    while True:
        val = q.get()
        print(f'{name}购买了第{val}辆大奔,当前线程{threading.currentThread()}')
        #
        time.sleep(1)


if __name__ == '__main__':

    print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
    # 创建出一个 队列 对象 q
    q = queue.Queue(4)

    # 创建线程
    # t1线程 发送数据
    t1 = threading.Thread(target=put_fn, args=('孙总', q))
    t2 = threading.Thread(target=put_fn, args=('肖总', q))
    t3 = threading.Thread(target=get_fn, args=('李老板', q))
    t4 = threading.Thread(target=get_fn, args=('韩董', q))
    t5 = threading.Thread(target=get_fn, args=('鑫总', q))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print(f'当前线程为{threading.currentThread()},当前时间为{time.time()}')
