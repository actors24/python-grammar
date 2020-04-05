# 通讯录程序

# 联系人列表
user_dict = {'黄嘉灵': 15536304304, '肖峰': 15545654445, '邓鹏': 12354564478}

# 进入主界面
print('''
|--- 欢迎进入通讯录程序 ---|
|--- 1：查询联系人资料 ----|
|--- 2：插入新的联系人 ----|
|--- 3：删除已有联系人 ----|
|--- 4：退出通讯录程序 ----|   
    ''')
while 1:
    query = input('请输入相关的指令代码：')
    if query == '1':
        #进入查询操作
        query1 = input('请输入联系人名字：')
        for i in user_dict:
            if query1 == i:
                print(f'{i}:{user_dict[i]}')
                break
        else:
            print('联系人不存在，请重试！')
    elif query == '2':
        #进入插入联系人界面
        query1 = input('请输入联系人名字：')
        for i in user_dict:
            if query1 == i:
                print('您输入的姓名在通讯录已存在 -->>')
                print(f'{i}:{user_dict[i]}')
                #修改现有联系人信息
                query2 = input('是否修改用户资料(YES/NO):')
                if query2 == 'YES':
                    query3 = input('请输入用户联系电话：')
                    user_dict[i] = query3
                    print('修改成功!')
                    print(f'{i}:{query3}')
                    break
                 # 不修改信息
                elif query2 == 'NO':
                    break
                else:
                    print('输入有误,请重新输入!')
                    break
        else:
            # 新增联系人信息
            query3 = input('请输入用户联系电话:')
            user_dict[query1] = query3
            print('添加成功!')
            print(f'{query1}:{query3}')
    elif query == '3':
        #进入删除联系人界面
        query1 = input('请输入联系人名字：')
        for i in user_dict:
            if query1 == i:
                user_dict.pop(i)
                print('删除成功！')
                break
        else:
            print('联系人不存在！')
    elif query == '4':
        break
    else:
        print('指令错误，请重新输入！')
