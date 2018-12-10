import pandas
import numpy
import fisher_2k





# 读取数据

fileName = 'I3.txt'    # 逐旬综合指标
file = open(fileName)    #划分依据
I0 = numpy.loadtxt(file)    # 逐旬综合指标
I0 = I0.tolist()
# print(I0)

# 初步划分，根据目前计算
I1 = I0[8:25]
I2 = I0[25:] + I0[:8]
I = [I1, I2]
#print(fisher_2k.fisher_I(I1))
#print(fisher_2k.fisher_I(I2))
#print(fisher_2k.fisher_I(I, 2))
print(fisher_2k.fisher_find(I0,I))
I3 = fisher_2k.fisher_huafen(I, 2)
print(I3)
print(fisher_2k.fisher_find(I0,I3))

I4 = fisher_2k.fisher_huafen(I3, 2)
#print(I[0])
print(I4)
print(fisher_2k.fisher_find(I0,I4))

#print(I)







# 计算位置
data_weizhi = fisher_2k.fisher_find(I0,I)
# n = fisher_2k.fisher_div(I2)
# print(data_weizhi)