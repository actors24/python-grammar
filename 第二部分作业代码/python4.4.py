sum=0
for i in range(101):
    if i%3==0 and i%5!=0:
        sum+=i
    else:
        continue
print(sum)
