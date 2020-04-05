def fun():
    return [lambda x: i * x for i in range(4)]


print([n(2) for n in fun()])
