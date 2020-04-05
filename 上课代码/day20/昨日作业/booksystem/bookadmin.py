import database
class BookAdmin:
    def __init__(self,name,pwd):
        self.name  = name
        self.pwd = pwd
    # 方法 登录
    def login(self):
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        for admin in database.admin_list: # 存放 是 一个一个 管理员对象  通过对象访问属性 比对
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
        database.admin_list.append(BookAdmin(name,pwd))

        print(database.admin_list)
    # 图书操作
    def add_book(self):
        # 增加图书
        name = input()
        author = input()
        price = input()
        press = input()
        database.book_list.append([name,price,author,press])
        print('添加图书成功')

