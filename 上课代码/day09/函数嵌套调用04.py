
def fn1():
    print('我是fn1')
    return True


def fn2():
    print('我是fn2')
    # 调用fn1 可以
    rst = fn1()
    if rst == True:
        print('今晚没有作业！')

fn1()
fn2()


# 晚上作业：
# 书写 判断质数 功能函数(其他处使用该函数)
# 声明函数，可以接收任何一个数字，并且可以对数字进行判断，是否为质数（通过 返回值 布尔值来体现）
# 打印输出100-200之内所有质数  函数式编程

# 判断功能函数 闰年
# 打印输出 1999-2019内所有的闰年  函数式编程


# 函数式编程：判断 年 月 日 日期是否合法  2019-2-29 不合法
'''
年月日，参数传递
年 不需要判断 
月 1-12 
日 匹配月份情况下 合法 1-30 1-31 1-28 1-29
'''


# def is_run_year(year):
#     if year % .....:
#         return True
#     else:
#         return False
#
#  #
#  def print_year(start,end):
#      for i in range(start,end+1):
#          rst = is_run_year(year)
#          if rst == True:
#              print()
#  print_year(1999,2019)