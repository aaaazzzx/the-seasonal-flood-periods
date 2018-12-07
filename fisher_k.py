# 对指定区间进行划分

import os
import pandas
import numpy

from sklearn.preprocessing import MinMaxScaler
from fisher_2k import fisher_I
from fisher_2k import fisher_div



if __name__ == '__main__':
    fileName = 'I3.txt'    # 逐旬综合指标
    pre_m = open(fileName)
    data = numpy.loadtxt(pre_m)    # 逐旬综合指标
    print(data)
    n, = data.shape
    # print(n)    #36
    # print (data_m_t)
    # D2 = numpy.zeros((y, x - 1, x - 1))  # 反期间
    # D1 = numpy.zeros((y, x))  # 仅去除一个  在旬中不考虑
    # D3 = numpy.zeros((y, x))  # 非首尾相连
    x = 0    # 指定连续期间
    y = 36
    z = range(x, y)
    # print(z)
    '''
    writer = pandas.ExcelWriter('fisher_xun指定位置.xlsx')
    I = numpy.zeros(y)  # 期间
    I2 = numpy.zeros(y)  # 期间
    for i in z:
            # I = numpy.zeros((y, i, i))  # 期间
        I[i] = i * numpy.std(data[x:i]) + (y - i) * numpy.std(data[i:y])
        I2[i] = fisher_I(data[x:i]) + fisher_I(data[i:y])
        # D3[k, i] = i * numpy.std(data_m_t[:i, k]) + (12*3 - i) * numpy.std(data_m_t[i:, k])
    print(I-I2)
    df = pandas.DataFrame(I)
    df.to_excel(writer, '%s-%s' % (x, y))
    writer.save()
    '''

    # 最优解
    #writer = pandas.ExcelWriter('fisher_最优分割.xlsx')
    x = 10
    y = 19
    data_in = data[10:19]
    a = fisher_I(data_in)
    #print(a)
    # print(fisher_div(data_in))
    data2 = data[:10]
    #data2.add(data[19:])
    # print(fisher_I(data2))





    # D2[k,i,j-1] = (12*3-(j-i+1)) * numpy.std ( numpy.append(data_m_t[:i,k],data_m_t[j:,k]) )

    #            for l in range(x):
    #                D1[k, l] = 11 * numpy.std(numpy.delete(data_m_t[:, k], l))
    # print (D2[1,:,:])

    # file = os.getcwd()
    # f = open('%s\data\pretreatment\D.txt'%(file),'w')
    # numpy.savetxt('%s\data\pretreatment\D.txt'%(file),D2[1,:,:])
    # f.close()

