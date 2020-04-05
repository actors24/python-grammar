
# 数据库信息 功能函数
def data():
    global admin_list
    global book_list
    # 管理员：账号 密码
    admin_list = [['weidong', '123']]
    # 书库
    book_list = [
        ['钢铁是怎样炼成的', 9.9, '孔祥泽', '李浩出版社'],
        ['坏蛋是怎样炼成的', 9.9, '磊哥', '磊哥出版社'],
        ['中华字典', 59.9, '康熙', '清朝出版社'],
        ['python从入门到精通', 29.9, '肖枫', '肖枫出版社'],
    ]


# 注册 功能函数
def register():
    name = input('请输入用户名:')
    if name in admin_list:
        print('账号已存在')
    else:
        pwd = input('请输入密码:')
        pwd1 = input('请输入密码:')
        #     添加到 数据库中 list中
        admin_list.append([name, pwd])
        print(admin_list)


# 图书管理功能函数

def book_admin():
#     操作？
    choice = input('请输入指令：查询 1 or 修改 2 or 删除 3 or 增加 4')
    if choice == '1':
        pass   # 查询功能函数调用
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    else:
        pass


# 登录 功能函数
def login(name,pwd):

    for admin in admin_list:
        if admin[0] == name and admin[1] == pwd:
            print('登录成功')
        #     调用 图书操作 功能函数
            book_admin()
        else:
            print('登录失败，请重新登录！')







# 主程序 完成 程序开发 主导   调用其他功能函数
# 初始情况
def main():
    data()
    print('欢迎使用图书管理系统')
    choice = input('请输入指令：注册 1 or 登录 2')
    if choice == '1': # 注册
        register()
    elif choice == '2':
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        login(name,pwd)
    else:
        print('指令有误！')

# 调用 主函数
main()