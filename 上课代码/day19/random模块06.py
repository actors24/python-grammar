
import random

#
num = random.random()
print(num) # 0-1区间 浮点型数字


#
int_num = random.randint(0,10)
print(int_num)


#
random_rst = random.choice('123456')
print(random_rst) # '6'

#
rst = random.randrange(0,10,2)
print(rst)


# 随机抽奖
l1 = ['李勇铭','孙总','鑫总','韩董','孔CTO','李CEO','李老板']
# 随机抽奖
# 下标：0 len(l1)-1
index = random.randint(0,len(l1))
# index = int(random.random() * 7)  # 0-1之间小数  0-6  0 1 2 3 456
name = l1[index]
# name = random.choice(l1)
print(f'恭喜{name}喜提193班第一阶段再来一次大奖！')


# Math.random() 0-1










