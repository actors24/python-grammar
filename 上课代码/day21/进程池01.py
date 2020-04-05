
# 批量创建进程 设置进程数量
import multiprocessing,time,os

def movie(name):
    for i in range(10):
        print(f'看电影{name},第{i}次，当前进程id为{os.getpid()}')
        time.sleep(0.01)


if __name__ == '__main__':

    print(f'当前时间为{time.time()},当前进程为{os.getpid()}')

    pool = multiprocessing.Pool(5)  # 对象

    for i in range(10):
        pool.apply_async(func=movie, args=('泰坦尼克号',))

    pool.close()

    pool.join()

    print(f'当前时间为{time.time()},当前进程为{os.getpid()}')
