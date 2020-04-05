sum=1
p=0
i=1
while 1:
    if sum%2!=0:
        p+=4/i
        sum+=1
        i+=2
    elif sum%2==0:
        p-=4/i
        sum+=1
        i+=2
    if 3.1415926<p<3.1415927:
        break
print(sum)
