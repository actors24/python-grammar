
# 图书管理系统升级
# 初级升级
# 书类- 属性 名字 价格 出版社 作者
# 管理员类- 属性 名字/密码  方法：图书增删改查  登录注册
# 库：书库 管理员库


# class DB:  # database 数据库




class Book:
    def __init__(self,name,price,author,press):
        self.name = name
        self.price = price
        self.author = author
        self.press = press

class BookAdmin:
    def __init__(self,name,pwd):
        self.name  = name
        self.pwd = pwd
    # 方法 登录
    def login(self):
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        for admin in admin_list: # 存放 是 一个一个 管理员对象  通过对象访问属性 比对
            if admin.name == name and admin.pwd == pwd:
                print('登录成功')
            #     图书管理 引导 输入指令？ 1 - 查询 2-修改 3-增加 4-删除
            #
                choice = input(' 1 - 查询 2-修改 3-增加 4-删除')
                if choice == '3':
                    self.add_book()

            else:
                print('登录失败，请重新登录！')

    # 注册用户
    def register(self):
        name = input('请输入用户名:')
        pwd = input('请输入密码:')
        pwd1 = input('请输入密码:')
        #     添加到 数据库中 list中
        admin_list.append(BookAdmin('伟东','123'))

        print(admin_list)
    # 图书操作
    def add_book(self):
        # 增加图书
        name = input()
        author = input()
        price = input()
        press = input()
        book_list.append([name,price,author,press])
        print('添加图书成功')


# 实例化对象
admin1 = BookAdmin('weidong','123')


admin_list = [BookAdmin('孔夫子','123')]  # admin对象
book_list = []