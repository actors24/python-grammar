a=int(input('请输入你的年龄:\n'))
if a<6:
    print('儿童')
elif 6<=a<=13:
    print('少年')
elif 14<=a<=17:
    print('青少年')
elif 18<=a<=35:
    print('青年')
elif 36<=a<=50:
    print('中年')
else:
    print('中老年')
