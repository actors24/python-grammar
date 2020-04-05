import threading
import time

class MovieThread(threading.Thread):
    def __init__(self,name,count):
        super().__init__()
        self.name = name # 电影名字
        self.count = count # 数量 次数

    def run(self):
        # 功能 要干什么
        for i in range(self.count):
            print(f"看电影{self.name},第{i}次,{threading.currentThread()}")

class MusicThread(threading.Thread):
    def __init__(self,name,count):
        super().__init__()
        self.name = name # 歌曲名字
        self.count = count # 数量 次数

    def run(self):
        # 功能 要干什么
        for i in range(self.count):
            print(f"听歌{self.name},第{i}次,{threading.currentThread()}")

if __name__ == '__main__':

    # mainThread 主线程
    time_str = time.time()
    print(f'当前时间为{time_str},当前线程{threading.currentThread()}')

    # 创建对象 线程
    # 新的线程 线程号 id
    t1 = MovieThread('娜扎',20)
    t2 = MusicThread('今天是个好日子',20)
    # 启动 线程
    t1.start()
    t2.start()

    time_str = time.time()
    print(f'当前时间为{time_str}当前线程{threading.currentThread()}')




