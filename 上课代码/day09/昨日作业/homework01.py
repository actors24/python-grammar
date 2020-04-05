
# str1 = "Aa.Bb.C,d,eF"   => "aA.bB.c,D,Ef"
# swapcase() 实现 大小写转换
str1 = "Aa.Bb.C,d,eF"
# print(str1.swapcase()) # aA.bB.c,D,Ef

# 判断
# 遍历 字符串，获取每个元素 判断 大写-小  小->大
sums = ''
for s in str1:
    new_s = s.lower()
    if s == new_s:
        new_s = s.upper()
    sums += new_s
print(sums)