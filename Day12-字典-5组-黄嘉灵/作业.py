# 1.
# a={'p':80,'y':121,'t':116,'h':104,'o':111,'n':110}
# print(a)

# 2.不正确,因为用花括号括起来的还有集合

# 3.会在这个字典新添加这个键值对

# 4.字典更高,因为字典使用的是哈希算法存储,每个键有自己的hash值,不需要使用查找算法,所以效率更高

# 5.键必须时不可变的，所以键的类型只能是不可变类型，而值可以取任何值

# 6.{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}
# {1: '数字', 3: '数字'}

# 7.是

# 8.dict2=dict1.copy()

# 9.
# # 通讯录程序
#
# # 联系人列表
# user_dict = {'黄嘉灵': 15536304304, '肖峰': 15545654445, '邓鹏': 12354564478}
#
# # 进入主界面
# print('''
# |--- 欢迎进入通讯录程序 ---|
# |--- 1：查询联系人资料 ----|
# |--- 2：插入新的联系人 ----|
# |--- 3：删除已有联系人 ----|
# |--- 4：退出通讯录程序 ----|
#     ''')
# while 1:
#     query = input('请输入相关的指令代码：')
#     if query == '1':
#         #进入查询操作
#         query1 = input('请输入联系人名字：')
#         for i in user_dict:
#             if query1 == i:
#                 print(f'{i}:{user_dict[i]}')
#                 break
#         else:
#             print('联系人不存在，请重试！')
#     elif query == '2':
#         #进入插入联系人界面
#         query1 = input('请输入联系人名字：')
#         for i in user_dict:
#             if query1 == i:
#                 print('您输入的姓名在通讯录已存在 -->>')
#                 print(f'{i}:{user_dict[i]}')
#                 #修改现有联系人信息
#                 query2 = input('是否修改用户资料(YES/NO):')
#                 if query2 == 'YES':
#                     query3 = input('请输入用户联系电话：')
#                     user_dict[i] = query3
#                     print('修改成功!')
#                     print(f'{i}:{query3}')
#                     break
#                  # 不修改信息
#                 elif query2 == 'NO':
#                     break
#                 else:
#                     print('输入有误,请重新输入!')
#                     break
#         else:
#             # 新增联系人信息
#             query3 = input('请输入用户联系电话:')
#             user_dict[query1] = query3
#             print('添加成功!')
#             print(f'{query1}:{query3}')
#     elif query == '3':
#         #进入删除联系人界面
#         query1 = input('请输入联系人名字：')
#         for i in user_dict:
#             if query1 == i:
#                 user_dict.pop(i)
#                 print('删除成功！')
#                 break
#         else:
#             print('联系人不存在！')
#     elif query == '4':
#         break
#     else:
#         print('指令错误，请重新输入！')

# 10.
# 初始化一个字典,用来存放用户信息
# user_list = dict()


# 定义新增用户函数
# def new_user(name, pwd):
#     for i in user_list:
#         if name == i:
#             print('此用户已被注册，请重新输入！')
#             break
#     else:
#         user_list[name] = pwd
#         print('注册成功，赶紧试试登陆吧^_^')
#         print(name, ':', pwd)
#
#
# # 定义用户登陆函数
# def login_user(name, pwd):
#     for i in user_list:
#         if name == i and pwd == user_list[i]:
#             print('欢迎进入用户登陆系统，请点击右上角的x结束程序！')
#             break
#     else:
#         print('该用户不存在，请重新输入！')
#
#
# while 1:
#     # 用户输入指令
#     query = input('''
#     | --- 新建用户：N/n ---|
#     | --- 登陆账号：E/e ---|
#     | --- 退出程序：Q/q ---|
#     | --- 请输入指令代码：
#     ''')
#     # 进入新增用户操作
#     if query == 'N' or query == 'n':
#         name = input("请输入用户名:")
#         if name == '':
#             print('用户名不能为空,请重新输入')
#             continue
#         pwd = input('请输入密码:')
#         if pwd == '':
#             print('密码不能为空,请重新输入')
#             continue
#         else:
#             new_user(name, pwd)
#             # 进入用户登陆操作
#     elif query == 'E' or query == 'e':
#         name = input("请输入用户名:")
#         pwd = input('请输入密码:')
#         login_user(name, pwd)
#         # 推出程序
#     elif query == 'Q' or query == 'q':
#         exit()
#     else:
#         print('指令有误，请重新输入！')
