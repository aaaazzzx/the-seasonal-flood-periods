# 首先构造D直径，其实并无必要

import os
import pandas
import numpy

from sklearn.preprocessing import MinMaxScaler


def eachFile(filename):
    file = os.getcwd()
    for root, dirs, files in os.walk(file):
        if filename in files:
            filePath = os.path.join(str(root), str(dirs))
            filePath = filePath[:-2] + filename
    return filePath


if __name__ == '__main__':
    fileName = 'I3.txt'
    filePath = eachFile(fileName)
    pre_m = open(filePath)
    data_m = numpy.loadtxt(pre_m)
    x, = data_m.shape
    # print (data_m_t)
    # D2 = numpy.zeros((y, x - 1, x - 1))  # 反期间
    # D1 = numpy.zeros((y, x))  # 仅去除一个  在旬中不考虑
    # D3 = numpy.zeros((y, x))  # 非首尾相连
    writer = pandas.ExcelWriter('fisher_xun.xlsx')
    I = numpy.zeros((x,x))  # 期间
    for i in range(1,x):
        # I = numpy.zeros((y, i, i))  # 期间
        # D3[k, i] = i * numpy.std(data_m_t[:i, k]) + (12*3 - i) * numpy.std(data_m_t[i:, k])
        for j in range(i):
            I[i, j ] = (j) * numpy.std(data_m[:j]) + ( i - j) * numpy.std(data_m[j:i])
    print(I)
    df = pandas.DataFrame(I[ :,:])
    df.to_excel(writer, 'k' )
    writer.save()
                # D2[k,i,j-1] = (12*3-(j-i+1)) * numpy.std ( numpy.append(data_m_t[:i,k],data_m_t[j:,k]) )

    #            for l in range(x):
    #                D1[k, l] = 11 * numpy.std(numpy.delete(data_m_t[:, k], l))
    # print (D2[1,:,:])

    # file = os.getcwd()
    # f = open('%s\data\pretreatment\D.txt'%(file),'w')
    # numpy.savetxt('%s\data\pretreatment\D.txt'%(file),D2[1,:,:])
    # f.close()

