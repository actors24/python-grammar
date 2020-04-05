w=float(input('please input the weight of goods:\n'))
if w<20:
    print('费用为',w*5)
elif 20<=w<100:
    print('费用为',100+(w-20)*0.2)
elif w>=100:
    print('费用为',100+16+(w-100)*0.15)
