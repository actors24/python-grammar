
#
# def fn1():
#     print('我是fn1函数')


# 进行自我介绍
# 我叫刘华山，我今年21岁了。
# 我叫肖枫，我今年3岁了。
# 我叫蒋浩楠，我今年18岁了。
# 我叫*，我今年*岁了。
# min() max(10,20,30,40)
# def intro(name,age):
#     print(f'我叫{name}，我今年岁{age}了。')

# 调用
# #  positional argument 位置参数
# intro('伟东',20) # 我叫伟东，我今年岁20了。
# intro('文韬',80) # 我叫文韬，我今年岁80了。
# intro(40,'鑫总') # 我叫40，我今年岁鑫总了。
# intro('鑫总',40)

# 关键字参数
# keyword argument
# format() 第三种方式
# intro(name='伟东',age=18) # 我叫伟东，我今年岁18了。
# intro(name=18,age='伟东') # 我叫伟东，我今年岁18了。
# intro(name=18,age=19) # 我叫伟东，我今年岁18了。

# 混用
# intro('伟东',age=18)
# intro(age=18,'伟东')

# sort(reverse=True) 排序 列表 升序
# 默认参数 default argument
# def intro(name,age=18):
#     print(f'我叫{name}，我今年岁{age}了。')
#
# #
# intro('小飞飞',18)
# intro('小飞飞',19)
# intro(age=20,name='小飞飞')


# 可变长参数
# arguments 多个参数
# def fn2(*args):
#     print(args)
#     for i in args:
#         print(i)
#
# # 调用
# fn2(10) # (10,)
# fn2(10,20,30,40,50) # (10, 20, 30, 40, 50)

# **kwargs  kw-keyword关键字 args 关键字参数
# def fn3(**kwargs):
# #     print(kwargs) # {'name': '鑫总', 'age': 18, 'addr': '沙河'} 字典 数据类型 列表 键值对
# #     for i in kwargs:
# #         print(i) #
# #
# # fn3(name='鑫总',age=18,addr='沙河')


# demo
def my_intro(name,age=18,*hobbys,**others):
    print(name,age)
    print(hobbys)
    print(others)
my_intro('蒋浩楠',18,"女",'男','打篮球','rap',other1='烫头',other2='抽烟',other3='喝酒')