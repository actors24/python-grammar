def fun6(i, j):
    if int((i * 10 + j) ** 0.5) == (i * 10 + j) ** 0.5:
        return True
    else:
        return False


for abc in range(100, 1000):
    if int(abc ** 0.5) == abc ** 0.5:
        a = abc // 100
        b = abc // 10 % 10
        c = abc % 10
        for xyz in range(100, 1000):
            if xyz != abc and int(xyz ** 0.5) == xyz ** 0.5:
                x = xyz // 100
                y = xyz // 10 % 10
                z = xyz % 10
                rst= fun6(a, x) + fun6(b, y) + fun6(c, z)
                if rst == 3:
                    print(abc, xyz)
