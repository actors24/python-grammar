
# 年份 练习题
# 判断 是否为闰年
def is_run_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

    return False

# 判断 日期是否合法
def legit_date(year,month,day):
#     判断？
    flag = False
    if month == 2:
    #     判断 平闰年
        if is_run_year(year):
            # 闰年 1-29
            if  1 <= day <= 29:
                flag = True
        else:
            # 平年
            if 1 <= day <= 28:
                flag = True
    elif month in [1,3,5,7,8,10,12]:  # day 1-31
        if 31 >= day >= 1:
            flag = True
    elif month in [4,6,9,11]: # day 1-30
        if 30 >= day >= 1:
            flag = True
    else:
        print('输入的月份无效，请重新输入')

    return flag
# 计算某个日期 是 当年的 第*天。2019-4-3  第 31 + 3  1.2.3月 天数之和 + 3
# 规律：当前月份之前的所有月份天数之和 + 当前日 数字
def count_day(year,month,day):
#     判断是否合法
    if legit_date(year,month,day) == True:
        # 合法 计算 当前月份之前所有月份 天数之和
        sums = 0
        for i in range(1,month): #  获取 当前月份之前的所有月份
    #         获取每个月份对应的天数   三大类  31 天 30 天   29.28
            if i == 2: # 2月份 28/29
                if is_run_year(year) == True:
                    sums += 29
                else:
                    sums += 28
            elif i in [1,3,5,7,8,10,12]: # 31天
                sums += 31
            elif i in [4,6,9,11]: # 30天
                sums += 30
        print(year,month,day,'为当年的第', sums + day,'天')

    else:
        print('日期不合法，请重新输入！')
count_day(2019,2,27)













