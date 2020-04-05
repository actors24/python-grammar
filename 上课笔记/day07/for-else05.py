
# for else
for i in range(5):
    print(i)  # 0 1 2 3 4
else:
    print('我是else代码块')

for i in range(5):
    print(i) # 0 1 2 3
    if i == 4:
        print('当前i为4')
        break # break
else:
    print('我是else代码块')

# 100-200内所有的质数  断点 endpoint
for i in range(100,201):  #
    for j in range(2,int(i**0.5) +1):
        if i % j == 0: # 说明不是质数 合数 j=2 3 4  5  6 7 8 9 10 102%2 == 0
            print(i,'不是质数')
            break
    else:
        print(i,'是质数') # 101