import multiprocessing
import os
import time


def movie(name):
    for i in range(20):
        print(f'看电影{name},第{i}次,当前进程{os.getpid()}')
        time.sleep(0.1)


def music(name,count):
    for i in range(count):
        print(f'听歌{name},第{i}次,当前进程{os.getpid()}')
        time.sleep(0.2)

if __name__ == '__main__':


    print(f'当前进程为{os.getpid()},当前时间为{time.time()}')

    # 创建对象
    # 使用类创建
    p1 = multiprocessing.Process(target=movie,args=('我和我的祖国',))
    p2 = multiprocessing.Process(target=music,args=('单身情歌',20),daemon=True)



    # 启动进程
    p1.start()
    p2.start()

    p1.join()
    # p2.join()



    print(f'当前进程为{os.getpid()},当前时间为{time.time()}')