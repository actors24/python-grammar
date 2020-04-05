1.append()
list1 = [10,20,30]
rst = list1.append(40)
print(list1) # [10, 20, 30, 40]
print(rst) # None
list1.append('123') # [10, 20, 30, 40, '123']
print(list1)
list1.append([True,False])
print(list1)

2.extend()
list1 = [10,20,30]
##rst = list1.extend('123')
##rst = list1.extend(range(11,15))
rst = list1.extend([40,50,60])
print(list1) # [10, 20, 30, 40, 50, 60]
print(rst) # None


3.insert()
list1 = [10,20,30]
##rst = list1.insert(1,40)
##rst = list1.insert(-3,'123')
rst = list1.insert(-5,[40,50])
print(list1) #['123', 10, 20, 30]
print(rst) # None


4.clear()
list1 = [10,20,30]
rst = list1.clear()
print(list1) # []
print(rst) # None


5.pop()
list1 = [10,20,30,40,50]
list1 = []
rst = list1.clear()
print(rst) # 10 弹栈
print(list1) # [20, 30, 40, 50]

6.remove()
list1 = [10,20,30,10,20,10,20]
rst = list1.remove(1)
print(list1)
print(rst)

7.copy()
list1 = [10,20,30]
rst = list1.copy()
print(list1) # [10, 20, 30]
print(rst) # [10, 20, 30]

8.count()
list1 = [10,20,30,10,20,10,20]
rst = list1.count(10)
print(rst) # 3
print(list1) # [10, 20, 30, 10, 20, 10, 20]

9.index()
list1 = [10,20,30,10,20,10,20]
rst = list1.index(10,0,3) # 3
print(rst)
print(list1) #[10, 20, 30, 10, 20, 10, 20]


10.reverse()
list1 = [10,20,30,40]
rst = list1.reverse()
print(rst) # None
print(list1) # [40, 30, 20, 10]

##11.sort() 排序 升序  降序
list1 = [70,25,10,1,7]
rst = list1.sort(reverse=True)
print(list1) #[1, 7, 10, 25, 70]
print(rst) #None











































