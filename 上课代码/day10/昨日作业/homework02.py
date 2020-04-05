
# 判断 是否为闰年

def is_run_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

    return False

# 打印 1999-2019年所有闰年
def print_year(start,end):
    for i in range(start,end+1):
        # 判断 i 是否为 闰年
        if is_run_year(i):
            print(i)

# print_year(1999,2019)


# 判断 日期是否合法
# 月 日 考察
'''
月：1-12月 
日：
    2月： 
        - 平年 1-28 
        - 闰年 1-29
    1 3 5 7 8 10 12:  1-31
    4 6 9 11: 1-30
    
'''
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
#     获取 flag变量 通过 它保存的值 判断当前日期是否合法
#     if flag == True:
#         print(year,month,day,'合法')
#     else:
#         print(year, month, day, '不合法')

    return flag


# input()
print(legit_date(2000,22,3))  #


# 某个日期，2000-2-3 是当年的第*天？