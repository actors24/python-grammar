
# FileNotFoundError 文件操作 open() 文件路径出现问题
# FileNotFoundError

class NoTicketError(Exception):
    def __init__(self, s):
        self.s = s
    def __str__(self):  # 类似 __init__() 方法 魔法方法-针对python
        print('我是__str__')
        return self.s

# t1 = NoTicketError(10) # t1 保存 首地址 代表 实例对象

# t1.__str__() # 不需要手动调用，会自动触发 类似__init__()
# print(t1) # 打印 t1 李辰昱  当实例对象作为字符串来访问时，会自动触发该方法


# 使用 自定义异常
# 买票时异常：没有票了

try:
    num = input('请输入数字')
    if int(num) == 10:  # 类型异常  False
        print('还有票，给你一张就行！')
    else:
        print('我想随便来个异常')
        raise NoTicketError('我是NoTicketError')

except NoTicketError as tips:
    print(tips) # 异常提示信息 异常参数 我是NoTicketError
    print('没有票啦！')


