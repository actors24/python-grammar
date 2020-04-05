a=[1,3,2,7,5]
l=len(a)
for i in range(l-1):
    for j in range(i+1,l):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
