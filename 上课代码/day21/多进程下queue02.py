
import multiprocessing,os,time

# 存放数据
def put_fn(q):
    l = [10,20,30,40,50,60]
    for i in l:
        q.put(i)
        print(f'当前存入queue中{i},当前进程为{os.getpid()}')
        time.sleep(1)

# 取数据
def get_fn(q):

    while True:
        # if q.empty():  # empty() 监听不一定为准
        #     break
        val = q.get(False)
        print(f'从queue中 取 {val},当前进程为{os.getpid()}')


if __name__ == '__main__':

    print(f'当前进程为{os.getpid()},当前时间为{time.time()}')
    # 队列
    q = multiprocessing.Queue()
    # 两个进程
    p1 = multiprocessing.Process(target=put_fn,args=(q,))
    p2 = multiprocessing.Process(target=get_fn,args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    p2.terminate()


    print(f'当前进程为{os.getpid()},当前时间为{time.time()}')
