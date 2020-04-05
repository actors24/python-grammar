
import time


# 1.sleep(seconds)
# print(123)
# time.sleep(10)
# print(456)

# 2.strftime()                 HOUR minute second
# 功能：时间格式化为 字符串 默认为当前时间
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # 2019-12-11 17:23:26


# 3.localtime()
# print(time.localtime())
#  0 -6 0-7 1-1 2-2 3-3 4-4 5-5 6-6
#  tm_wday 表？
# time.struct_time(tm_year=2019, tm_mon=12, tm_mday=11, tm_hour=17, tm_min=25, tm_sec=55, tm_wday=2, tm_yday=345, tm_isdst=0)


# 4.time()
# 时间戳
# 距离1970 1 1 0:0:0 累积的 秒数
# 毫秒  1000
print(time.time()) # 1576056597.495293