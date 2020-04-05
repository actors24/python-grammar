##list1 = [10,20,[30,40]]
## 访问 内部列表中 第一个元素
## 列表[下标]
##print(list1[2])  #[30, 40]
##list2 = list1[2]  #[30, 40]
##print(list1[2][0])
##l = [1,2,[2,3,[4,5,6]],5,[7,8,9,5]]
##print(l[2][2][0])  

##
list1 = [10,20,[30,40]]
for i in list1:
    
##    if typ e(i) == list:
    if isinstance(i,list) == True:
        for j in i:
            print(j)
    else:
        print(i)


