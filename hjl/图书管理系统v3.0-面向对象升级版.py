user_dict = {'jialing': '123'}
admin_dict = {'admin': '123'}
book_list = [['钢铁是怎样炼成的', '9.9', '尼古拉斯', '国学出版社']]


class User:
    def user_register(self):
        name = input('请输入你的用户名:')
        pwd = input('请输入你的密码')
        for i in user_dict.keys():
            if i == name:
                print('该用户已存在!')
                self.user_register()
                break
        else:
            print('注册成功!')
            user_dict[name] = pwd

    def user_login(self):
        name = input('请输入你的名字：')
        pwd = input('请输入你的密码:')
        for i in user_dict.keys():
            if i == name and user_dict[i] == pwd:
                UserBookManage()
                break
        else:
            print('用户名或密码错误，请重新输入！')
            self.user_login()


class Admin:

    def admin_register(self):
        name = input('请输入你的用户名:')
        pwd = input('请输入你的密码')
        for i in admin_dict.keys():
            if i == name:
                print('该用户已存在!')
                self.admin_register()
                break
        else:
            print('注册成功!')
            admin_dict[name] = pwd
            self.admin_login()

    def admin_login(self):
        name = input('请输入你的名字：')
        pwd = input('请输入你的密码:')
        for i in admin_dict.keys():
            if i == name and admin_dict[i] == pwd:
                BookManage().book_manage()
                break
        else:
            print('用户名或密码错误，请重新输入！')
            self.admin_login()


class BookManage:
    def book_manage(self):
        choice = input('请输入你的操作：1.查看所有图书 2.增加图书 3.删除图书 4.修改图书 5.查询图书 6.查看所有用户 7.退出程序')
        if choice == '1':
            self.show_book_all()
        elif choice == '2':
            self.book_add()
        elif choice == '3':
            self.book_del()
        elif choice == '4':
            self.book_mod()
        elif choice == '5':
            self.book_serach()
        elif choice == '6':
            self.show_user_all()
        elif choice == '7':
            exit()
        else:
            print('输入有误，请重新输入!')
            self.book_manage()

    def show_book_all(self):
        for i in book_list:
            print(f'书名:{i[0]} 价格:{i[1]} 作者{i[2]} 出版社:{i[3]}')
        self.book_manage()

    def book_add(self):
        name = input('请输入书籍名字:')
        for i in book_list:
            if i[0] == name:
                print('该书籍已存在!')
                self.book_manage()
        else:
            price = input('请输入金额:')
            author = input('请输入作者:')
            org = input('请输入出版社:')
            print('添加成功!')
            book_list.append([name, price, author, org])
        self.book_manage()

    def book_del(self):
        name = input('请输入书籍名字:')
        for i in book_list:
            if i[0] == name:
                book_list.remove(i)
                print('删除成功!')
                self.book_manage()
        else:
            print('该书籍不存在!')
            self.book_manage()

    def book_mod(self):
        name = input('请输入书籍的名字:')
        for i in book_list:
            if i[0] == name:
                query1 = input('请输入你要修改书籍的信息: 1.名字 2.金额 3.作者 4.出版社')
                if query1 == '1':
                    new_name = input('请输入新名字:')
                    i[0] = new_name
                    print('修改成功!')
                elif query1 == '2':
                    new_price = input('请输入新金额:')
                    i[1] = new_price
                    print('修改成功!')
                elif query1 == '3':
                    new_author = input('请输入新作者:')
                    i[2] = new_author
                    print('修改成功!')
                elif query1 == '4':
                    new_org = input('请输入新出版社:')
                    i[3] = new_org
                    print('修改成功!')
                self.book_manage()

        else:
            print('该书籍不存在!')
            self.book_manage()

    def book_serach(self):
        query2 = input('请输入你要查询的信息: 1.书名 2.金额 3.作者 4.出版社')
        if query2 == '1':
            name = input('请输入书籍名字:')
            for i in book_list:
                if i[0] == name:
                    print(f'书名:{i[0]} 价格:{i[1]} 作者{i[2]} 出版社:{i[3]}')
                    self.book_manage()
            else:
                print('符合该条件的书籍不存在!')
                self.book_manage()
        elif query2 == '2':
            price = input('请输入书籍金额:')
            for i in book_list:
                if i[1] == price:
                    print(f'书名:{i[0]} 价格:{i[1]} 作者{i[2]} 出版社:{i[3]}')
                    self.book_manage()
            else:
                print('符合该条件的书籍不存在!')
                self.book_manage()
        elif query2 == '3':
            author = input('请输入书籍作者:')
            for i in book_list:
                if i[2] == author:
                    print(f'书名:{i[0]} 价格:{i[1]} 作者{i[2]} 出版社:{i[3]}')
                    self.book_manage()
            else:
                print('符合该条件的书籍不存在!')
                self.book_manage()
        elif query2 == '4':
            org = input('请输入书籍出版社:')
            for i in book_list:
                if i[3] == org:
                    print(f'书名:{i[0]} 价格:{i[1]} 作者{i[2]} 出版社:{i[3]}')
                    self.book_manage()
            else:
                print('符合该条件的书籍不存在!')
                self.book_manage()

    def show_user_all(self):
        for i in user_dict.keys():
            print(f'用户名:{i} 密码:{user_dict[i]}')
        self.book_manage()


class UserBookManage:
    def show_book_all(self):
        pass

    def book_search(self):
        pass


class Menu:
    print('''
---------------------------------

欢迎进入图书管理系统（对象升级版）

---------------------------------
''')
    while 1:
        query = input('''
        **********************
        请输入你要进行的操作：
            1.注册用户
            2.用户登陆
            3.管理员注册
            4.管理员登陆
            5.退出程序
        **********************
        ''')
        if query == '1':
            User().user_register()
        elif query == '2':
            User().user_login()
        elif query == '3':
            Admin().admin_register()
        elif query == '4':
            Admin().admin_login()
        elif query == '5':
            exit()
        else:
            print('输入有误,请重新输入!')
