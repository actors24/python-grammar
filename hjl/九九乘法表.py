# 矩形输出九九乘法表
for a in range(1, 10):
    for b in range(1, 10):
        print(a, '*', b, '=', a * b, end='\t')
    print()
print()
# 左下九九乘法表
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(j, '*', i, '=', j * i, end='\t')
        else:
            break
    print()
print()
# 右下九九乘法表
for c in range(1, 10):
    for d in range(1, 9 - c + 1):
        print('        ', end='\t')
    for e in range(1, c + 1):
        print(c, '*', e, '=', c * e, end='\t')
    print()
print()
# 左上乘法表
for f in range(1, 10):
    for g in range(f, 10):
        print(f, '*', g, '=', f * g, end='\t')
    print()
print()
# 右上乘法表
for h in range(1, 10):
    for j in range(1, h):
        print('        ', end='\t')
    for k in range(h, 10):
        print(h, '*', k, '=', h * k, end='\t')
    print()
