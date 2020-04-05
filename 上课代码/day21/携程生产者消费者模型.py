# 消费者
def consumer():
    r = ''
    while True:
        n = yield r  # yield生成器 拿到数据 通过n保存
        if not n:
            return
        print('consumer 消费了 %s' % n)  # 消费者取数据
        r = 'ok'  # 执行完毕

# 生产者
def producer(c):
    c.send(None)  # 开启 生成器
    n = 0
    while n < 5:
        n += 1
        print('producer 生产了 %s' % n)  # 一旦生产了东西，就会通过send()发送
        r = c.send(n)
        print('consumer 返回了 %s' % r)
    c.close()


c = consumer()
producer(c)
