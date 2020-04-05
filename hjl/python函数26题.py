def fun3(a, b, c):
    if (b ** 2 - 4 * a * c) < 0:
        print(str(a) + 'x**' + str(2) + '+' + str(b) + 'x' + '+' + str(c) + '=0' + '无根')
    elif (b ** 2 - 4 * a * c) == 0:
        x = (-b) / 2 * a
        print(str(a) + 'x**' + str(2) + '+' + str(b) + 'x' + '+' + str(c) + '=0' + '的根为' + str(x))
    elif (b ** 2 - 4 * a * c) > 0:
        x1 = ((b ** 2 - 4 * a * c) ** 0.5 - b) / (2 * a)
        x2 = ((-b) - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        print(str(a) + 'x**' + str(2) + '+' + str(b) + 'x' + '+' + str(c) + '=0' + '的根为' + str(x1) + '和' + str(x2))


fun3(1, 4, 2)
