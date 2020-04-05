m = int(input('请输入第一个数：'))
n = int(input('请输入第二个数：'))
row = 0
list1 = 0
q = 1
value = 1
l = list()
l = [[i] * n for i in range(m)]
a = 'b'
while value <= m * n:
    if a == 'b':
        l[row][list1] = value
        if list1 >= n - q:
            a = 'c'
            continue
        list1 += 1
    if a == 'c':
        l[row][list1] = value
        if row >= m - q:
            a = 'd'
            continue
        row += 1
    if a == 'd':
        l[row][list1] = value
        if list1 <= q - 1:
            a = 'e'
            continue
        list1 -= 1
    if a == 'e':
        l[row][list1] = value
        if row - 1 <= q:
            a = 'b'
            q += 1
        row -= 1
    value += 1
for j in l:
    print(j)
