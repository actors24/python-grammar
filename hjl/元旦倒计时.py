import time

time1 = time.mktime((2020, 1, 1, 0, 0, 0, 0, 0, 0))
while 1:
    time2 = time1 - time.time()
    days = time2 // (3600 * 24)
    hours = (time2 % (3600 * 24)) // 3600
    minutes = (time2 % (3600 * 24) % 3600) // 60
    seconds = (time2 % (3600 * 24) % 3600) % 60
    print(f'现在距离元旦还有{int(days)}天，{int(hours)}时，{int(minutes)}分，{int(seconds)}秒')
    time.sleep(1)
