# 初始化一个字典,用来存放用户信息
user_list = dict()


# 定义新增用户函数
def new_user(name, pwd):
    for i in user_list:
        if name == i:
            print('此用户已被注册，请重新输入！')
            break
    else:
        user_list[name] = pwd
        print('注册成功，赶紧试试登陆吧^_^')
        print(name, ':', pwd)


# 定义用户登陆函数
def login_user(name, pwd):
    for i in user_list:
        if name == i and pwd == user_list[i]:
            print('欢迎进入用户登陆系统，请点击右上角的x结束程序！')
            break
    else:
        print('该用户不存在，请重新输入！')


while 1:
    # 用户输入指令
    query = input('''
    | --- 新建用户：N/n ---|
    | --- 登陆账号：E/e ---|
    | --- 退出程序：Q/q ---|
    | --- 请输入指令代码：
    ''')
    # 进入新增用户操作
    if query == 'N' or query == 'n':
        name = input("请输入用户名:")
        if name == '':
            print('用户名不能为空,请重新输入')
            continue
        pwd = input('请输入密码:')
        if pwd == '':
            print('密码不能为空,请重新输入')
            continue
        else:
            new_user(name, pwd)
            # 进入用户登陆操作
    elif query == 'E' or query == 'e':
        name = input("请输入用户名:")
        pwd = input('请输入密码:')
        login_user(name, pwd)
        # 推出程序
    elif query == 'Q' or query == 'q':
        exit()
    else:
        print('指令有误，请重新输入！')
