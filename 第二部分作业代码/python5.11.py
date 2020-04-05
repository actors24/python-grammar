a=[1,3,2,7,5]
l=len(a)
for i in range(l):
    for j in range(1,l-i):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
print(a)
