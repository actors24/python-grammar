
try:
    a = 10
    b = 20
    # a / 0  #  0不能做除数
    print('我是6行')
except ValueError as tip1:
    print(tip1,'valueError')
except ZeroDivisionError as tip2:
    print(tip2,'ZeroDivisionError')
else:
    print('我是else代码块')
finally: # 无论如何都会执行
    print('我是finall代码块')

# for - else
