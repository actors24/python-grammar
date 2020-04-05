for i in range(1,101):
    for j in range(1,101):
        for z in range(1,101):
            if i+j+z*3==100:
                if i*3+j*2+z==100:                
                    print(i,j,3*z)
    


