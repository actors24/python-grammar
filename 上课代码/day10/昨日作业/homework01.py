
# 书写 一个 判断质数的 功能函数
#
def is_zhi_shu(num):
    # 判断质数
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    # else:
    return True
# is_zhi_shu(9)

# 函数编程 打印输出 100-200之间所有的质数
def print_zhishu(start,end):
    # start end 两个数字 进行比较 最小值 最大值
    # max_num = start if start > end else end
    '''
    :param start: the start of iterable a int a number
    :param end:
    :return: None   -> None
    '''
    for i in range(start,end):
        # 对每个元素i进行 判断 是否为质数
        # rst = is_zhi_shu(i)
        if is_zhi_shu(i):
            print(i,'质数')

print_zhishu(100,200)