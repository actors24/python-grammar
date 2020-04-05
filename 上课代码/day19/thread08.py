

'''
创建方式二：
    使用父类创建
'''
import time
import threading


# 看电影
def watch_movie(name,count):
    for i in range(count):
        print(f"看电影{name},第{i}次,{threading.currentThread()}")
        time.sleep(0.5)

# 听歌
def listen_to_music(name,count):
    for i in range(count):
        print(f"听歌{name},第{i}次,{threading.currentThread()}")
        time.sleep(0.4)


if __name__ == '__main__':

    now_time = time.time()
    print(f'当前线程为{threading.currentThread()},当前时间为{now_time}')

    # 创建线程对象
    t1 = threading.Thread(target=watch_movie,args=('娜扎',20),name='t1')
    t2 = threading.Thread(target=listen_to_music,args=('今天是个好日子',20))

    # 启动对象
    t1.start()
    t2.start()

    #
    t2.setName('t2')

    #



    now_time = time.time()
    print(f'当前线程为{threading.currentThread()},当前时间为{now_time}')