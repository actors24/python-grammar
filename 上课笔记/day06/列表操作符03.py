list1 = [1,2,3]
list2 = [4,5,6]
print(list1 + list2) # [1, 2, 3, 4, 5, 6]
print(list1)
print(list2)
print(list1 + [10]) # [1, 2, 3, 10]

##2. *
##print([1,2,3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]


## 3. in / not in
##print(3 in [1,2,3]) # True
##print(3 not in [1,2,3]) # False
## 判断一下 某个元素是否存在于列表中？
## 1.使用 in not in
## 2.使用for循环 逐一进行判断
## 3. 列表常用方法 count()  (也可考虑 index() remove())

##4. 比较运算符

 列表中元素进行一一比较，一旦比较出大小，则停止
 列表中元素数据类型要一致，否则比较会报错，typeError
list1 = [1,2,3]
list2 = [4,5,6]
print(list1 > list2) # False
##
list3 = [10,'abc',True]
list4 = ['ef',12,False]
print(list3 > list4)

list3 = [10,11]
list4 = [9.5,12]
print(list3 > list4)

## 字符串 比较 每个字符ASCII值
list3 = ['ab','ec','df']
list4 = ['ef','ac','bd']
print(list3 > list4 and list3 < list4) # False






















