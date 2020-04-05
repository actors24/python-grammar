import random

while 1:
    a = int(random.randint(1, 3))
    if a == 1:
        b = '石头'
    if a == 2:
        b = '剪刀'
    if a == 3:
        b = '布'
    m = input('请输入石头，剪刀，布：')
    if m not in ['石头', '剪刀', '布']:
        print('输入有误，请重新输入!')
    else:
        if m == b:
            print(f'电脑出{b},平手')
        elif m == '石头' and b == '剪刀' or m == '剪刀' and b == '布' or m == '布' and b == '石头':
            print(f'电脑出{b},你赢了!')
        elif m == '石头' and b == '布' or m == '剪刀' and b == '石头' or m == '布' and b == '剪刀':
            print(f'电脑出{b},你输了!')
