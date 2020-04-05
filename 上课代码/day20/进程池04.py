
import multiprocessing
import os
import time

def movie(name):
    for i in range(5):
        print(f'看电影{name},第{i}次,当前进程{os.getpid()}')
        time.sleep(0.1)


if __name__ == '__main__':


    pool = multiprocessing.Pool(5)

    # 创建进程
    # 执行任务目标
    for i in range(10):
        pool.apply_async(func=movie, args=('我和我的祖国',))


    # 关闭 进程池
    pool.close()

#     join()
# terminate()
    pool.join()

