for i in range(1,37):
    for j in range(1,37):
        for z in range(1,37):
            if i+j+z*2==36:
                if 4*i+3*j+z==36:
                    print(i,j,z*2)
    
