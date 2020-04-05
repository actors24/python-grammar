for i in range(1000,10000):
    d=i%10
    c=i//10%10
    b=i//100%10
    a=i/1000
    if (a*b+c*d)*(a*b+c*d)==a*b*c*d:
        print(i)
