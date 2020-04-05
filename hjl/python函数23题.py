def fun2(*list1):
    a, b, c, d = 0, 0, 0, 0
    sums = 0
    for i in list1:
        for j in i:
            if '0' <= j <= '9':
                a += 1
            elif 'a' <= j <= 'z' or 'A' <= j <= 'Z':
                b += 1
            elif j == ' ':
                c += 1
            else:
                d += 1
        sums += 1
        print('第', sums, '个字符串有:', b, '个英文', a, '个数字', c, '个空格', d, '个字符')


fun2('hello world,gada  +2231233', 'sdfaffaf', '25dsf')
