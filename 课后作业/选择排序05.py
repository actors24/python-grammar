list1 = [7,1,3,5,4,2,8,6]
for i in range(len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]


print(list1)
