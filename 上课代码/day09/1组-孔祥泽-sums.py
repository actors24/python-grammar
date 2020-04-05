def sums(iterable, start = 0):
    for i in iterable:
        start += i
    return start
print(sums([12, 123,23],10))
