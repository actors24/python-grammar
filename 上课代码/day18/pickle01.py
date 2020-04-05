

#
# f = open('1.txt','wb')

# f.write([10,20,30,40])

# 写入 列表
# f.writelines([10,20,30,40])

#
import pickle

# l1 = [10,20,30,40]
# # dump(obj,file) write()
# pickle.dump(l1,f)
#
# print(f.closed)
# f.close()


# 读
f = open('1.txt','rb')
import pickle
rst = pickle.load(f)
print(rst) # [10, 20, 30, 40]
# upload上传 download下载


# json序列化
# dump() load()