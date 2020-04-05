##
### 自定义模块 当前模块名字 module01
##
### 内容：
##
##a = 10
##
##
##def fn():
##    print('我是module01中的fn函数')
##
##
##class A:
##    name = 'module01_A'
##
##    def a_fn(self):
##        print('我是class A中的a方法')
##    def __chenxi(self):
##        print('我要打陈曦')
##
### print(__name__) # __main__  module01
##
##if __name__ == '__main__':  # 主要的
##    # 测试 打印语句
##    print('我是module01的打印语句')
##

n=input('请输入文件名:')
f=open(n,'w')
m=input('请输入内容:【单独输入":w"保存退出】:')
f.writelines(m)
