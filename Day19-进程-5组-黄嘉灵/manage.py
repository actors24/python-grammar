import database as b
import object as a
import pickle


class Manage:


    def __init__(self):
        self.userDB = b.UserDB()

        self.userDB.add(a.User('jialing', '123'))
        self.userDB.add(a.User('jiahao', '123'))
        self.bookDB = b.BookDB()
        self.bookDB.add(a.Book('sss', '12.0', 'asd', 'df'))
        self.bookDB.add(a.Book('sss', '12.0', 'asd', 'we'))
        self.adminDB = b.AdminDB()
        self.adminDB.add(a.Admin('admin', '123'))
        with open('1.txt','rb') as f1:
            rst=pickle.load(f1)
            self.adminDB._AdminDB__admin_list=rst
        with open('2.txt','rb') as f3:
            rst1=pickle.load(f3)
            self.userDB._UserDB__user_list=rst1

    def login_query(self):
        query = input('1.管理员登陆 2.普通用户登陆 3.返回上一级 4.退出程序')
        if query == '1':
            self.admin_login()
        elif query == '2':
            self.user_login()
        elif query == '3':
            self.start()
        elif query == '4':
            exit()
        else:
            print('输入有误!')
            self.login_query()

    def admin_login(self):
        name = input('请输入管理用户名:')
        pwd = input('请输入密码:')
        if self.adminDB.select_one_admin(a.Admin(name, pwd)):
            print('欢迎进入系统!')
            self.manage()
        else:
            print('账号或密码有误!')
            self.login_query()

    def user_login(self):
        name = input('请输入用户名:')
        pwd = input('请输入密码:')
        if self.userDB.select_one_user(a.User(name, pwd)):
            print('欢迎进入系统!')
            self.user_manage()
        else:
            print('账号或密码有误!')
            self.login_query()

    def welcome(self):
        print('********欢迎进入图书管理系统**********')
        r = input('1:登陆 2.注册 3.退出程序')
        return r

    def register_query(self):
        query = input('1.管理员注册 2.普通用户注册 3.返回主页面 4.退出程序')
        if query == '1':
            self.admin_register()
        elif query == '2':
            self.user_register()
        elif query == '3':
            self.start()
        elif query == '4':
            exit()
        else:
            print('输入有误!')
            self.register_query()

    def admin_register(self):
        name = input('请输入管理用户名:')
        if self.adminDB.admin_exists(a.Admin(name, 0)):
            print('此管理员已注册！')
            self.register_query()
        else:
            while 1:
                pwd = input('请输入密码:')
                pwd1 = input('请确认密码:')
                if pwd != pwd1:
                    print('密码不一致，请重新输入!')
                else:
                    self.adminDB.add(a.Admin(name, pwd))
                    print('注册成功!')
                    with open('1.txt','wb') as f:
                        pickle.dump(self.adminDB._AdminDB__admin_list,f)
                        f.close()
                    self.register_query()

    def user_register(self):
        name = input('请输入用户名:')
        if self.userDB.user_exists(a.User(name, 0)):
            print('此用户已注册！')
            self.register_query()
        else:
            while 1:
                pwd = input('请输入密码:')
                pwd1 = input('请确认密码:')
                if pwd != pwd1:
                    print('密码不一致，请重新输入!')
                else:
                    self.userDB.add(a.User(name, pwd))
                    print('注册成功!')
                    with open('2.txt','wb') as f2:
                        pickle.dump(self.userDB._UserDB__user_list,f2)
                        f2.close()
                    self.register_query()

    def main(self):
        while 1:
            r = self.welcome()
            if r == '1':
                self.login_query()
            elif r == '2':
                self.register_query()
            elif r == '3':
                exit()
            else:
                print('指令错误!')
                self.welcome()

    def start(self):
        self.main()

    def manage(self):
        while 1:
            n = input('请输入你要进行的操作: 1.增加书籍 2.删除书籍 3.修改书籍 4.查询书籍 5.查看所有书籍 6.查看所有用户 7.返回上级 8.返回主页面 9.退出程序')
            if n == '1':
                self.add_book()
            elif n == '2':
                self.delete_book()
            elif n == '3':
                self.change_book()
            elif n == '4':
                self.show_book()
            elif n == '5':
                self.show_all_book()
            elif n == '6':
                self.show_all_user()
            elif n == '7':
                self.login_query()
            elif n == '8':
                self.start()
            elif n == '9':
                exit()
            else:
                print('指令错误!')

    def user_manage(self):
        while 1:
            n = input('请输入要进行的操作: 1.查看图书 2.查看所有图书 3.返回上一级 4.返回主页面 5.退出程序')
            if n == '1':
                self.show_book()
            elif n == '2':
                self.show_all_book()
            elif n == '3':
                self.login_query()
            elif n == '4':
                self.start()
            elif n == '5':
                exit()
            else:
                print('指令错误')

    def add_book(self):
        name = input('请输入要增加的书名:')
        if self.bookDB.select_one_book(name):
            print('该书籍已存在!')
        else:
            price = input('请输入价格:')
            author = input('请输入作者:')
            org = input('请输入出版社:')
            self.bookDB.add(a.Book(name, price, author, org))
            print('添加成功!')

    def delete_book(self):
        name = input('请输入要删除的书籍:')
        book = self.bookDB.select_one_book(name)
        if book:
            self.bookDB.delete(book)
            print('删除成功!')
        else:
            print('该书不存在!')

    def change_book(self):
        name = input('请输入要修改的书名:')
        book = self.bookDB.select_one_book(name)
        if book:
            r = input('1.修改书名 2.修改价格 3.修改作者 4.修改出版社 5.返回上一级 6.退出程序')
            if r == '1':
                new_name = input('请输入新书名')
                book.name = new_name
                print('修改成功!')
                self.bookDB.modify(book)
            elif r == '2':
                price = input('请输入新价格:')
                book.price = price
                print('修改成功!')
                self.bookDB.modify(book)
            elif r == '3':
                author = input('请输入新作者:')
                book.author = author
                print('修改成功!')
                self.bookDB.modify(book)
            elif r == '4':
                org = input('请输入新出版社:')
                book.org = org
                print('修改成功!')
                self.bookDB.modify(book)
            elif r == '5':
                pass
            elif r == '6':
                exit()
            else:
                print('指令有误!')
        else:
            print('该书不存在!')

    def show_book(self):
        n = input('请输入要查询的信息: 1.书名 2.价格 3.作者 4.出版社 5.返回上一级 6.退出程序')
        if n == '1':
            name = input('请输入书名:')
            # self.bookDB.select_one_book1(name)
            if self.bookDB.select_one_book1(name) == 0:
                print('该书籍不存在!')
        elif n == '2':
            price = input('请输入金额:')
            # self.bookDB.select_one_book2(price)
            if self.bookDB.select_one_book2(price) == 0:
                print('该书籍不存在!')
        elif n == '3':
            author = input('请输入作者:')
            # self.bookDB.select_one_book3(author)
            if self.bookDB.select_one_book3(author) == 0:
                print('该书籍不存在!')
        elif n == '4':
            org = input('请输入出版社:')
            # self.bookDB.select_one_book4(org)
            if self.bookDB.select_one_book4(org) == 0:
                print('该书籍不存在!')
        elif n == '5':
            pass
        elif n == '6':
            exit()
        else:
            print('指令错误!')
            self.show_book()

    def show_all_book(self):
        self.bookDB.select()

    def show_all_user(self):
        self.userDB.select()
        self.manage()
