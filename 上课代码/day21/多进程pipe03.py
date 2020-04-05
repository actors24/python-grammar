import multiprocessing,os,time

# 存放数据
def send_fn(p):
    l = [10,20,30,40,50,60]
    for i in l:
        p[1].send(i)
        print(f'当前存入queue中{i},当前进程为{os.getpid()}')
        time.sleep(1)

# 取数据
def recv_fn(p):

    while True:
        # if q.empty():  # empty() 监听不一定为准
        #     break
        val = p[0].recv()
        print(f'从queue中 取 {val},当前进程为{os.getpid()}')


if __name__ == '__main__':

    print(f'当前进程为{os.getpid()},当前时间为{time.time()}')
    # 管道 Pipe
    p = multiprocessing.Pipe()  # 生成元组 两个元素-分别代表管道两头 (conn1,conn2)

    p1 = multiprocessing.Process(target=send_fn,args=(p,))
    p2 = multiprocessing.Process(target=recv_fn,args=(p,))

    p1.start()
    p2.start()

    p1.join()

    print(f'当前进程为{os.getpid()},当前时间为{time.time()}')
