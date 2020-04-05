y = int(input("which year do you want to count:"))
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    d = 366
else:
    d = 365
print(d * 24 * 60 * 60)
