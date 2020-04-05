a=10

def fn():
    print('我是module01中的fn函数')

class A:
    name='module01_A'

    def a_fn(self):
        print('我是class A中的a方法')
    def __hehe(self):
        print('hehe')


# print(__name__)

if __name__=='__main__':
    print('我是module01的打印语句')