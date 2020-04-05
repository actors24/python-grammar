
f1 = input('请输入一个文件')
f2 = input('请输入第二个文件')

ff1 = open(f1,'r',encoding='utf-8')
ff2 = open(f2,'r',encoding='utf-8')

# 读取
rst1 = ff1.readlines()
rst2 = ff2.readlines()


# 遍历 列表
count = 0
if len(rst1) <= len(rst2):
    for i in range(len(rst1)): # 以短为准
        if rst1[i] != rst2[i]:
            print('第',i+1,'行不同')
            count += 1
else:
    for i in range(len(rst2)):  # 以短为准
        if rst2[i] != rst1[i]:
            print('第',i+1,'行不同')
            count += 1
print(count) # 4


ff1.close()
ff2.close()