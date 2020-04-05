
'''
特殊赋值：

'''
# a = b = c = 10
# print(a)
# print(b)
# print(c)
# # print()

# 创建字典
# print(dict(['34','12'])) # {'3': '4', '1': '2'}
# d1 = {}
# for k,v in ['34','12']:
#     print(k,v) # k,v = '34' '12'

#
# a,b = '12'
# a,b = [10,20]
# a,b = (10,20)
# a,b = {1,2}
# a,b = range(2)
# a,b = {'k':10,'v':20}
# print(a)
# print(b)

# s = 'html'
# a,b = s[0],s[1:]
# print(a)
# print(b)


# a,*b = 'html'
# print(a) # 'h'
# print(b) # ['t', 'm', 'l']

#
# a,*b,c = 'html'
# print(a) # 'h'
# print(b) # ['t', 'm' ]
# print(c) # 'l'

# a,*b,b = 'html'
# print(a) # 'h'
# print(b) # 'l'

# a,*b,c,d = 'html'
# print(a) # 'h'
# print(b) # ['t']
# print(c) # 'm'
# print(d) # 'l'

# a,*b,c,d,e = 'html'
# print(a) # 'h'
# print(b) # []
# print(c) # 't'
# print(d) # 'm'
# print(e) # 'l'

# a,*b,c,d,e,f = 'html'
# print(a) # 'h'
# print(b) # []
# print(c) # 't'
# print(d) # 'm'
# print(e) # 'l'

# a,*b,c,**d = 'html'
# print(a) # 'h'
# print(b) # []
# print(c) # 't'
# print(d) # 'm'
# print(e) # 'l'


'''
作业：
    - 当天代码 一遍
    - 整理思维导图 增加今日内容
    - 进程线程作业
    - 复习
进程线程协程：
    - 什么是进程？进程特点
    - 什么是线程？进程 线程 关系
    - 什么是多线程？
    - GIL 是什么？
    - 什么是多进程？
    - Lock 有什么意义？RLock 有什么意义？
    - 什么是 协程？ 理解 优势 缺点 你个人理解 demo
    - 代码
        - 创建线程 进程 方法  使用
        - Lock 代码
        - 进程池创建 
        - 进程间通信    Queue Pipe queue.Queue 
'''