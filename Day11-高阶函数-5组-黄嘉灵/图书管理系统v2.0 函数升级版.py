# 数据库信息 功能函数
def data():
    global admin_list
    global book_list
    # 管理员：账号 密码
    admin_list = [['jialing', '123'],['jiahao','456']]
    # 书库
    book_list = [
        ['钢铁是怎样炼成的', '9.9', '孔祥泽', '李浩出版社'],
        ['坏蛋是怎样炼成的', '9.9', '磊哥', '磊哥出版社'],
        ['中华字典', '59.9', '康熙', '清朝出版社'],
        ['python从入门到精通', '29.9', '肖枫', '肖枫出版社'],
    ]


# 注册 功能函数
def register():
    name = input('请输入用户名:')
    for i in admin_list:
        if name == i[0]:
            print('账号已存在,请重新输入')
            register()
    else:
        pwd = input('请输入密码:')
        pwd1 = input('请输入密码:')
        if pwd==pwd1:
            #     添加到 数据库中 list中
            admin_list.append([name, pwd])
            print('注册成功!')
            print(admin_list)
        else:
            print('密码不一致,请重新输入!')
            register()


# 图书管理功能函数

def book_admin():
    #     操作？
    choice = input('请输入指令：增加 1 or 删除 2 or 修改 3 or 查询 4  or 返回 5 or 查看全部书籍 6 ')
    if choice == '1':
        book_add()
    elif choice == '2':
        book_del()
    elif choice == '3':
        book_mod()
    elif choice == '4':
        book_res()
    elif choice=='5':
        return None
    elif choice=='6':
        print(book_list)
        book_admin()
    else:
        print('输入有误,请重新输入')
        book_admin()

# 增加图书操作
def book_add():
    book_name = input('请输入想要增加的书籍名字')
    for i in book_list:
        if book_name == i[0]:
            print('当前书籍存在,请重新输入!')
            book_admin()
    else:
        book_price = input('请输入书籍价格:')
        book_author = input('请输入书籍作者:')
        book_org = input('请输入书籍出版社:')
        book_list.append([book_name, book_price, book_author, book_org])
        print('添加成功!')
        print(book_list)
        book_admin()


# 图书删除操作
def book_del():
    sum3=0
    book_name = input('请输入你要删除的书籍:')
    for i in book_list:
        if book_name == i[0]:
            book_list.remove(i)
            print('书籍删除成功!')
            sum3+=1
            book_admin()
    if sum==0:
        print('当前书籍不存在!,请重新输入')
        book_admin()


# 图书修改信息操作
def book_mod():
    book_name = input('请输入你要修改的书籍名字:')
    for i in book_list:
        if book_name == i[0]:
            sum2=0
            query = input('请输入你要修改的信息: 1.名字 2.价格 3.作者 4.出版社')
            if query == '1':
                new_book_name = input('请输入书籍名字:')
                i[0] = new_book_name
                print('修改成功!')
                print(i)
                sum2+=1
                book_admin()
            elif query == '2':
                new_book_price = input('请输入价格:')
                i[1] = new_book_price
                print('修改成功!')
                print(i)
                sum2+=1
                book_admin()
            elif query == '3':
                new_book_author = input('请输入作者:')
                i[2] = new_book_author
                print('修改成功!')
                print(i)
                sum2+=1
                book_admin()
            elif query == '4':
                new_book_org = input('请输入出版社:')
                i[3] = new_book_org
                print('修改成功!')
                print(i)
                sum2+=1
                book_admin()
    if sum2==0:
        print('当前书籍不存在,请重新输入!')
        book_admin()
            # 图书查询操作


def book_res():
    query = input('请输入你要查询的书籍索引: 1.书名 2.价格 3.作者 4.出版社 5.返回')
    if query == '1':
        sums = 0
        book_name = input('请输入你要查询的书名:')
        for i in book_list:
            if book_name == i[0]:
                print(f'书名:{i[0]} 价格:{i[1]} 作者:{i[2]} 出版社:{i[3]}')
                sums += 1
        if sums == 0:
            print('当前书名不存在,请重新输入')
        book_res()
    elif query == '2':
        sums = 0
        book_price = input('请输入你要查询的价格:')
        for i in book_list:
            if book_price == i[1]:
                print(i)
                sums += 1
        if sums == 0:
            print('当前价格不存在,请重新输入')
        book_res()
    elif query == '3':
        sums = 0
        book_author = input('请输入你要查询的作者:')
        for i in book_list:
            if book_author == i[2]:
                print(i)
                sums += 1
        if sums == 0:
            print('当前书名不存在,请重新输入')
        book_res()
    elif query == '4':
        sums = 0
        book_org = input('请输入你要查询的出版社:')
        for i in book_list:
            if book_org == i[3]:
                print(i)
                sums+=1
        if sums == 0:
            print('当前书名不存在,请重新输入')
        book_res()
    elif query=='5':
        book_admin()
    else:
        print('输入有误,请重新输入!')
        book_res()

            # 登录 功能函数


def login():
    name = input('请输入用户名：')
    pwd = input('请输入密码：')
    sums1=0
    for i in admin_list:
        if i[0] == name and i[1] == pwd:
            print('登录成功')
            #     调用 图书操作 功能函数
            book_admin()
            sums1+=1
    if sums1==0:
        print('登录失败，请重新登录！')
        login()


# 主程序 完成 程序开发 主导   调用其他功能函数
# 初始情况
def main():
    data()
    print('欢迎使用图书管理系统')
    while 1:
        choice = input('请输入指令：注册 1 or 登录 2  查看所有用户  3')
        if choice == '1':  # 注册
            register()
        elif choice == '2':
            login()
        elif choice=='3':
            print(admin_list)
        else:
            print('指令有误！')


# 调用 主函数
main()
