
# 1.写入内容
fl = input('请输入文件名')
f = open(fl,'w',encoding='utf-8')

print('请输入要写的内容: :w停止')

while True:
    content1 = input()
    if content1 != ':w':
        f.write(content1 + "\n")
    else:
        break
f.close()