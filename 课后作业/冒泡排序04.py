list1 = [7,1,3,5,4,2,8,6]
for i in range(len(list1)-1):
    for j in range(len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list1)
