# 自定义异常

# class NoTicketError(Exception):
#     def __init__(self, *args, **kwargs):
#         pass
#
# # 使用自定义异常
# try:
#     num=int(input('请输入数字:'))
#     if num==10:
#         print('还有票!')
#     else:
#         raise NoTicketError('我是NoTicketError')
# except NoTicketError as tips:
#     print(tips)
#     print('没有票啦')

# class A:
#     def __init__(self,s):
#         self.s=s
#     def __str__(self):
#         return self.s
#
# print(A('10'))

# 自动关闭文件
# with open('1.txt') as f:    #with的作用：自动关闭文件
#     print(f.read())
#
#
# print(f.closed)

# 使用异常捕获文件操作
# try:
#     with open('2.txt') as f:  # with的作用：自动关闭文件
#         print(f.read())
# except:
#     print('文件不存在')

# try-except-else
# try:
#     a=10
#     b=20
#     a/2
#     print('我是呵呵')
# except ValueError as tips:
#     print(tips,'valueerror')
#
# except ZeroDivisionError as tips2:
#     print(tips2,'zeroerror')
# else:
#     print('我是else代码块')
# finally:
#     print('hello')

# for-else:
# for i in range(5):
#     print(i)
#     if i>3:
#         break
# else:
#     print('hehe')

# while-else:
# n=0
# while n<10:
#     print(n)
#     n+=1
#     if n>5:
#         break
# else:
#     print('dfas')

# randomm模块
# num=random.random()
# print(num)
#
# int_num=random.randint(1,10)
# # print(int_num)
#
# import random
#
# random_num=random.choice('123456')
# print(random_num)

# rst=random.randrange(0,10,2)
# print(rst)

# import random
#
# print(f'{["asd", "ssa", "sda", "sgs", "wrsf", "234rf"][random.randint(0, 4)]}')

# 进程线程
# thread
# 方式一
# import threading
# import time
#
#
# class MovieThread(threading.Thread):
#     def __init__(self, name, count):
#         super().__init__()
#         self.name = name
#         self.count = count
#
#     def run(self):
#         # 功能，要干什么
#         for i in range(self.count):
#             print(f'看电影{self.name},第{i}次')
#
#
# if __name__ == '__main__':
#     # mainThread 主线程
#     print(f'当前时间为{time.time()}')
#
#     # 创建对象线程
#     t1 = MovieThread('jianling', 5)
#     # 启动线程
#     t1.start()
#
#     print(f'当前时间为{time.time()}，hehe')

# 方式二
# 使用父类创建
# import time
# import threading
#
# def watch_movie(name,count):
#     for i in range(count):
#         print(f'看电影{name},第{i}次，{threading.currentThread()}')
#         time.sleep(0.3)
#
# def listen_music(name,count):
#     for i in range(count):
#         print(f'听歌{name},第{i}次，{threading.currentThread()}')
#         time.sleep(0.2)
#
# if __name__=='__main__':
#     now_time=time.time()
#     print(f'当前线程为{threading.currentThread()}，当前时间为{now_time}')
#
#     t1=threading.Thread(target=watch_movie,args=('哪吒',20),name='t1')
#     t2 = threading.Thread(target=watch_movie, args=('七里香', 20), name='t2')
#
#     t1.start()
#     t2.start()
#
#     now_time = time.time()
#     print(f'当前线程为{threading.currentThread()}，当前时间为{now_time}')
