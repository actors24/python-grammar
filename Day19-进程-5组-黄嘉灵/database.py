class BookDB:
    __book_list = []

    def select(self):
        for i in self.__book_list:
            print(i.name, i.price, i.author, i.org)

    def modify(self, book):
        for i in self.__book_list:
            if i.name == book.name:
                i.price = book.price
                i.author = book.author
                i.org = book.org
                return True
        else:
            return False

    def add(self, book):
        self.__book_list.append(book)

    def delete(self, book):
        self.__book_list.remove(book)

    def select_one_book(self, name):
        for i in self.__book_list:
            if i.name == name:
                return i
        else:
            return False

    def select_one_book1(self, name):
        sums = 0
        for i in self.__book_list:
            if i.name == name:
                print(i.name, i.price, i.author, i.org)
                sums += 1
        if sums == 0:
            return 0

    def select_one_book2(self, price):
        sums = 0
        for i in self.__book_list:
            if i.price == price:
                print(i.name, i.price, i.author, i.org)
                sums += 1
        if sums == 0:
            return 0

    def select_one_book3(self, author):
        sums = 0
        for i in self.__book_list:
            if i.author == author:
                print(i.name, i.price, i.author, i.org)
                sums += 1
        if sums == 0:
            return 0

    def select_one_book4(self, org):
        sums = 0
        for i in self.__book_list:
            if i.org == org:
                print(i.name, i.price, i.author, i.org)
                sums += 1
        if sums == 0:
            return 0


class UserDB:
    __user_list = []

    def select(self):
        for i in self.__user_list:
            print(i.name, i.pwd)

    def add(self, user):
        self.__user_list.append(user)

    def user_exists(self, user):
        for i in self.__user_list:
            if i.name == user.name:
                return True
        else:
            return False

    def select_one_user(self, user):
        for i in self.__user_list:
            if i.name == user.name and i.pwd == user.pwd:
                return True
        else:
            return False


class AdminDB:
    __admin_list = []

    def add(self, admin):
        self.__admin_list.append(admin)

    def admin_exists(self, admin):
        for i in self.__admin_list:
            if i.name == admin.name:
                return True
        else:
            return False

    def select_one_admin(self, admin):
        for i in self.__admin_list:
            if i.name == admin.name and i.pwd == admin.pwd:
                return True
        else:
            return False