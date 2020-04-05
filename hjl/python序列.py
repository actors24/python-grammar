def add(*arg):
    plus = 0
    for i in arg:
        plus += int(i)
    return plus


print(add(2, 3, 4, 1, 2, 3))
