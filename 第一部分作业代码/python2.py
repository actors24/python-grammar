y=int(input('请输入要查询的年份:\n'))
if y%4==0 and y%100!=0 or y%400==0:
      print(366*24*60*60)
else:
      print(365*24*60*60)
