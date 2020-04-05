import random
# print(random.random())#随机生成等一个浮点数
# print(round(random.random(),5))#随机生成等一个浮点数，可以通过round方法设置小数点后的位数


# print(random.randint(100000,1000000))#从a-b区间中选取一个随机数并返回
# print(random.randint(10,100))#从a-b区间中选取一个随机数并返回
# print(random.randint(100,1000))#从a-b区间中选取一个随机数并返回


#3.choice(self, seq)
# l=[1,2,32,4,24,3,63,57,5]
# t=(12,35,135,46,73,7,3,46,4)
# s='回家狗开狙击啊阿'
# d={'1':4,'3':8}
# print(random.choice(l)) #从一个序列中随机选取一个值并返回
# print(random.choice(t))
# print(random.choice(s))
# print(random.choice(d))

# 4.randrange(self, start, stop=None, step=1)#返回range[start,stop)之间的一个整数，可加step，跟range(0,10,2)类似

# print(random.randrange(0, 23))
# print(random.randrange(23))
# print(random.randrange(23,1,-1))
# print(random.randrange(0, 23, 2))


# 5.choices(self, population, weights=None, *, cum_weights=None, k=1)
# 3.6版本新增。从population集群中随机抽取K个元素（可重复）。
# weights是相对权重列表，cum_weights是累计权重，两个参数不能同时存在。

# print(random.choices('12345',weights=(1,21,23,24,100),k=10))

# 6.random.sample(population, k)
# 从population样本或集合中随机抽取K个重复的元素形成新的序列。常用于不重复的随机抽样。
# print(random.sample('3213gydguqu', k = 6))
# print(random.sample([1,32,25,23,67,322,5,1,32,25,23,67,322,5], k = 3))
# print(random.sample((1,32,25,23,67,322,5), k = 6))
# print(random.sample({1,32,25,23,67,322,5}, k = 6))

#7random.shuffle(x[, random])
# 随机打乱序列x内元素的排列顺序。只能针对可变的序列
# l=[1, 2, 24, 5, 3, 6, 8]
# random.shuffle(l)
# print(l)

#8random.triangular(low, high, mode)
# 返回一个low <= N <=high的三角形分布的随机数。参数mode指明众数出现位置。



