l1 = [1,4,10,3,5,2]

n = len(l1) # 6

for i in range(1,n):  # i = 1,  i=2  i=3  i=4 i=5
    for j in range(i,n):  # range(5,6)
        if l1[i - 1] > l1[j]: #  l1[4] >    l1[5]
            l1[i-1],l1[j] = l1[j],l1[i-1]
print(l1)  