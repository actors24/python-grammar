# 管理员信息库
# 管理员：账号，密码
admin_list = [['jialing', '123'], ['jiaan', '456'], ['jiahao', '789']]
# 书库，其中包括
book_list = [
    ['钢铁是怎样炼成的', '9.9', 'kongxiangze', 'lihaochubanshe'],
    ['换单是怎样来弄成的', '19.9', 'leige', 'leigechubanshe'],
    ['zhonghuazidian', '59.9', 'kangxi', 'qingchaochubanshe'],
    ['pythonshizenyanglianchengde', '20.1', 'xiaofeng', 'xiaofengchubanshe'],
    ['钢铁是怎样炼成的', '19.9', 'kangxi', 'xiaofengchubanshe']
]
# 系统开始界面
print('''
********************

欢迎来到图书管理系统

********************
''')
# 进行业务操作

# 登陆操作
# 保证系统能够重新运作
while 1:
    sum2 = 0
    # 提示数额u语句，让用户选择登陆还是注册
    choice = input('''
********************
    请输入指令:
    1.用户登陆
    2.用户注册
********************\n
    ''')
    # 进入登陆操作
    if choice == '1':
        # 登陆验证
        # 输入用户名，密码
        name = input('请输入用户名:')
        pwd = input('请输入密码:')
        # 让输入的信息与数据库的数据对比，如果存在则登录成功
        for admin in admin_list:
            if admin[0] == name and admin[1] == pwd:
                print('登陆成功!')
                sum2 += 1
                while 1:
                    # 用户进行增删改差操作
                    n = input('''
    ********************
    请输入你想做的操作：
    1.增加书籍 
    2.删除书籍 
    3.修改书籍 
    4.查询书籍
    5.查询全部书籍
    6.返回上一级
    ********************
                     ''')
                    # 进入增加书籍界面
                    if n == '1':
                        while 1:
                            book_name = input('请输入书籍名称:\n')
                            # 将输入的书名与数据库进行对比
                            for i in book_list:
                                if book_name == i[0]:
                                    print('该书籍已存在!')
                                    break
                            else:
                                # 添加书籍信息到数据库
                                book_age = input('请输入书籍价格!')
                                book_author = input('请输入作者:')
                                book_org = input('请输入出版社:')
                                question1 = input('确定添加? 1.是 2.否')
                                if question1 == '1':
                                    book_list.append([book_name, book_age, book_author, book_org])
                                    print('添加成功!')
                                    print(book_list)
                                else:
                                    break
                            # 询问是否返回菜单
                            query1 = input('返回菜单？1.是 2.否')
                            if query1 == '1':
                                break
                    # 进入书籍删除操作
                    elif n == '2':
                        sum3 = 0
                        while 1:
                            book_name = input('请输入你要删除的书籍名字：')
                            for i in book_list:
                                if book_name == i[0]:
                                    question2 = input('确定删除? 1.是 2.否')
                                    if question2 == '1':
                                        # 将相关书籍从数据库中移除
                                        book_list.remove(i)
                                        print('删除成功')
                                        sum3 += 1
                                    else:
                                        break
                            if sum3 == 0:
                                print('此书籍不存在！')
                            query2 = input('返回菜单？1.是 2.否')
                            if query2 == '1':
                                break
                    # 进入书籍修改操作
                    elif n == '3':
                        while 1:
                            sum4 = 0
                            book_name = input('请输入你要修改的书籍名字：')
                            for i in book_list:
                                if book_name == i[0]:
                                    # 询问要修改什么额信息
                                    query = input('''
    ********************
    请输入你要修改的信息：
    1.书籍名字 
    2.书籍价格 
    3.书籍作者 
    4.书籍出版社
    ********************
                                    ''')
                                    # 修改书籍名字
                                    if query == '1':
                                        new_book_name = input('请输入你要修改的名字：')
                                        sum4 += 1
                                        question3 = input('确定修改? 1.是 2.否')
                                        if question3 == '1':
                                            i[0] = new_book_name
                                            print('修改成功，修改后的信息为：', i)
                                        else:
                                            break
                                        # 修改书籍价格
                                    elif query == '2':
                                        new_book_age = input('请输入你要修改的价格:')
                                        sum4 += 1
                                        question3 = input('确定修改? 1.是 2.否')
                                        if question3 == '1':
                                            i[1] = new_book_age
                                            print('修改成功，修改后的信息为：', i)
                                        else:
                                            break
                                        # 修改书籍作者
                                    elif query == '3':
                                        new_book_author = input('请输入你要修改的作者：')
                                        sum4 += 1
                                        question3 = input('确定修改? 1.是 2.否')
                                        if question3 == '1':
                                            i[2] = new_book_author
                                            print('修改成功，修改后的信息为：', i)
                                        else:
                                            break
                                        # 修改书籍出版社
                                    elif query == '4':
                                        new_book_org = input('请输入你要修改的出版社:')
                                        sum4 += 1
                                        question3 = input('确定修改? 1.是 2.否')
                                        if question3 == '1':
                                            i[3] = new_book_org
                                            print('修改成功，修改后的信息为：', i)
                                        else:
                                            break
                            if sum4 == 0:
                                print('该书籍不存在')
                            query3 = input('返回菜单？1.是 2.否')
                            if query3 == '1':
                                break
                    # 进入书籍查询操作
                    elif n == '4':
                        sum1 = 0
                        # 询问用户要根据什么来进行查询
                        query = input('''
    ********************
    请输入你要查询的索引：
    1.书籍名字 
    2.书籍价格 
    3.书籍作者 
    4.书籍出版社
    ********************
                        ''')
                        # 根据书籍名字来查找
                        if query == '1':
                            while 1:
                                book_name = input('请输入你要查询的书籍名字')
                                for i in book_list:
                                    if book_name == i[0]:
                                        print(i)
                                        sum1 += 1
                                if sum1 == 0:
                                    print('该书籍不存在')
                                query4 = input('返回菜单？1.是 2.否')
                                if query4 == '1':
                                    break
                        # 根据书籍价格来查找
                        elif query == '2':
                            while 1:
                                book_age = input('请输入你要查询的书籍价格')
                                for i in book_list:
                                    if book_age == i[1]:
                                        print(i)
                                        sum1 += 1
                                if sum1 == 0:
                                    print('该书籍不存在')
                                query5 = input('返回菜单？1.是 2.否')
                                if query5 == '1':
                                    break
                        # 根据书籍作者来查找
                        elif query == '3':
                            while 1:
                                book_author = input('请输入你要查询的书籍作者')
                                for i in book_list:
                                    if book_author == i[2]:
                                        print(i)
                                        sum1 += 1
                                if sum1 == 0:
                                    print('该书籍不存在')
                                query6 = input('返回菜单？1.是 2.否')
                                if query6 == '1':
                                    break
                        # 根据书籍出版社来进行查找
                        elif query == '4':
                            while 1:
                                book_org = input('请输入你要查询的书籍出版社')
                                for i in book_list:
                                    if book_org == i[3]:
                                        print(i)
                                        sum1 += 1
                                if sum1 == 0:
                                    print('该书籍不存在')
                                query7 = input('返回菜单？1.是 2.否')
                                if query7 == '1':
                                    break
                    # 输出全部书籍信息
                    elif n == '5':
                        for i in book_list:
                            print(i)
                    # 返回上一级菜单
                    elif n == '6':
                        break
                    else:
                        print('输入有误，请重新输入!')

            # 操作 图书管理
            # 增加
            # 删除 某一本书？列表 查找？保证能够找到，删除
            # 改 修改 哪一本修改什么信息？价格？作者？
            # 查 查询 通过书名？作者？价格？出版社？ 打印输出 当前查询到的所有的书的信息 格式清晰
        # 如果输入的数据与数据库不匹配，则登陆失败
        # 登陆失败，重新操作
        if sum2 == 0:
            print('登陆失败,请重新登陆!')
    # 进入注册操作
    elif choice == '2':
        # 注册
        # 先输入用户名，判断数据库中是否以存在
        # 保证用户名可用，在输入密码，二次验证 最终添加到数据库
        # 用户名已存在则再次输入用户名
        while 1:
            sum5 = 0
            name = input('请输入用户名：')
            # 输入的用户名与数据库做对比
            for i in admin_list:
                if name in i[0]:
                    print('该账号已存在,请重新输入!')
                    break
            # 用户名正确继续输入密码
            else:
                while 1:
                    pwd = input('请输入密码:')
                    pwd1 = input('请再次确认密码:')
                    # 判断两次密码是否一致
                    if pwd != pwd1:
                        print('密码不一致，请重新输入!')
                        # 两次密码一致，注册成功
                    else:
                        # 将个人信息添加到数据库
                        sum5 = + 1
                        question4 = input('确定注册? 1.是 2.否')
                        if question4 == '1':
                            admin_list.append([name, pwd])
                            print('注册成功!')
                            print(admin_list)
                            question5 = input('是否返回到主菜单？ 1.是 2.否')
                            if question5 == '1':
                                break
                            else:
                                sum5 += 1
                        else:
                            question5 = input('是否返回到主菜单？ 1.是 2.否')
                            if question5 == '1':
                                break
                            else:
                                sum5 += 1
                    if sum5 == 2:
                        break
            # 注册成功，返回到首页面
            if sum5 == 1:
                break
    # 指令有误
    else:
        print('指令有误，请重新输入!')
