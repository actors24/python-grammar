
'''
通讯录登录程序
    - 注册账号 N/n
        - 验证 账号是否已经存在，如果存在，重新输入
    - 登录账号 E/e
        - 登录验证
    - 退出程序 Q/q
        - 退出程序
函数式编程

'''

# 主函数 调用其他函数 完成当前程序
import sys

# 数据库
user_list = {'user1':'123'}


# 创建 注册 函数
# 允许 输入用户名 判断库是否已存在，如果存在，重新输入，否则 输入密码，添加数据
def register():
    while True:
        name = input('请输入用户名:')
        if name in user_list:
            print('用户名已存在，请重新输入!')
        else:
            break
    pwd = input('请输入密码:')
    #         添加到数据库中
    user_list[name] = pwd
    print('注册成功，赶紧试试吧！')

# 登录
# 登录 账号 密码
# 判断账号是否存在，存在 再输入密码，不存在 重新输入
def login():
    while True:
        name = input('请输入用户名:')
        if name in user_list:
            print('用户名存在！')
            pwd = input('请输入密码：')
            if user_list[name] == pwd:
                print('验证成功，登录成功')
                break
        else:
            print('用户名不存在，请重新输入')





def run():

    while True:
        print("""
            |---新建用户：N/n---|
            |---登录账号：E/e---|
            |---退出程序：Q/q---|    
            """)
        choice = input('请输入指令:')
        if choice in ['N', 'n']:
            print('注册用户')
            register()
        elif choice in ['E', 'e']:
            print('登录')
            login()
        elif choice == 'Q' or choice == 'q':
            print('欢迎下次使用')
            # break
            # 程序退出
            sys.exit()
        else:
            print('指令输入有误，请重新输入')

run()















