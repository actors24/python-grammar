

import os

# os.remove(r'.\abc02.py')

# 删除 5.txt文件

os.remove(r'..\..\..\5.txt')

# print(os.listdir('..'))


'''
./ : 表示当前目录 
../  ： 表示上一级目录
如果还有需要继续返回上一级 ..\..\ 以此类推
'''