class Book:
    def __init__(self, name, price, author, org):
        self.name = name
        self.price = price
        self.author = author
        self.org = org


class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class BookDB:
    book_list = []

    def select(self):
        for i in self.book_list:
            print(i.name, i.price, i.author, i.org)

    def modify(self, book):
        for i in self.book_list:
            if i.name == book.name:
                i.price = book.price
                i.author = book.author
                i.org = book.org
                return True
        else:
            return False

    def add(self, book):
        self.book_list.append(book)

    def delete(self, book):
        self.book_list.remove(book)

    def select_one_book(self, name):
        for i in self.book_list:
            if i.name == name:
                return i
        else:
            return False

    def select_one_book1(self, name):
        for i in self.book_list:
            if i.name == name:
                print(i.name, i.price, i.author, i.org)

    def select_one_book2(self, price):
        for i in self.book_list:
            if i.price == price:
                print(i.name, i.price, i.author, i.org)

    def select_one_book3(self, author):
        for i in self.book_list:
            if i.author == author:
                print(i.name, i.price, i.author, i.org)

    def select_one_book4(self, org):
        for i in self.book_list:
            if i.org == org:
                print(i.name, i.price, i.author, i.org)


class UserDB:
    __user_list = []

    def select(self):
        for i in self.__user_list:
            print(i.name, i.pwd)

    def add(self, user):
        self.__user_list.append(user)

    def select_one_user(self, user):
        for i in self.__user_list:
            if i.name == user.name and i.pwd == user.pwd:
                return True
        else:
            return False


class Manage:
    def __init__(self):
        self.userDB = UserDB()
        self.userDB.add(User('jialing', '123'))
        self.userDB.add(User('admin', '123'))
        self.bookDB = BookDB()
        self.bookDB.add(Book('sss', '12.0', 'asd', 'df'))
        self.bookDB.add(Book('sss', '12.0', 'asd', 'we'))

    def login(self):
        name = input('请输入用户名:')
        pwd = input('请输入密码:')
        if self.userDB.select_one_user(User(name, pwd)):
            print('欢迎进入系统!')
            self.manage()

        else:
            print('账号或密码有误!')

    def welcome(self):
        print('********欢迎进入图书管理系统**********')
        r = input('1:登陆 2.注册 3.查看所有用户')
        return r

    def register(self):
        name = input('请输入用户名:')
        pwd = input('请输入密码:')
        if self.userDB.select_one_user(User(name, pwd)):
            print('此用户已注册！')
            self.register()
        else:
            self.userDB.add(User(name, pwd))

    def main(self):
        while 1:
            r = self.welcome()
            if r == '1':
                self.login()
            elif r == '2':
                self.register()
            elif r == '3':
                UserDB().select()
            else:
                print('指令错误!')
                self.welcome()

    def start(self):
        self.main()

    def manage(self):
        n = input('请输入你要进行的操作: 1.增加书籍 2.删除书籍 3.修改书籍 4.查询书籍 5.查看所有书籍 6.返回上一级')
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
            self.start()
        else:
            print('指令错误!')
            self.manage()

    def add_book(self):
        name = input('请输入要增加的书名:')
        if self.bookDB.select_one_book(name):
            print('该书籍已存在!')
            self.manage()
        else:
            price = input('请输入价格:')
            author = input('请输入作者:')
            org = input('请输入出版社:')
            self.bookDB.add(Book(name, price, author, org))
            print('添加成功!')
            self.manage()

    def delete_book(self):
        name = input('请输入要删除的书籍:')
        book = self.bookDB.select_one_book(name)
        if book:
            self.bookDB.delete(book)
            print('删除成功!')
            self.manage()
        else:
            print('该书不存在!')
            self.manage()

    def change_book(self):
        name = input('请输入要修改的书名:')
        book = self.bookDB.select_one_book(name)
        if book:
            r = input('1.修改书名 2.修改价格 3.修改作者 4.修改出版社 5.返回上一级')
            if r == '1':
                new_name = input('请输入新书名')
                book.name = new_name
                print('修改成功!')
                self.bookDB.modify(book)
                self.manage()
            elif r == '2':
                price = input('请输入新价格:')
                book.price = price
                print('修改成功!')
                self.bookDB.modify(book)
                self.manage()
            elif r == '3':
                author = input('请输入新作者:')
                book.author = author
                print('修改成功!')
                self.bookDB.modify(book)
                self.manage()
            elif r == '4':
                org = input('请输入新出版社:')
                book.org = org
                print('修改成功!')
                self.bookDB.modify(book)
                self.manage()
            elif r == '5':
                self.manage()
            else:
                print('指令有误!')
                self.manage()
        else:
            print('该书不存在!')
            self.manage()

    def show_book(self):
        n = input('请输入要查询的信息: 1.书名 2.价格 3.作者 4.出版社 5.返回上一级')
        if n == '1':
            name = input('请输入书名:')
            self.bookDB.select_one_book1(name)
            self.manage()
        elif n == '2':
            price = input('请输入金额:')
            self.bookDB.select_one_book2(price)
            self.manage()
        elif n == '3':
            author = input('请输入作者:')
            self.bookDB.select_one_book3(author)
            self.manage()
        elif n == '4':
            org = input('请输入出版社:')
            self.bookDB.select_one_book4(org)
            self.manage()
        elif n == '5':
            self.manage()
        else:
            print('指令错误!')
            self.show_book()

    def show_all_book(self):
        self.bookDB.select()
        self.manage()


Manage().start()
