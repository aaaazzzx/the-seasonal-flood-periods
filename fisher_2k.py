# 将其分成三段

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


def fisher_I(data):    # 对指定的区间进行计算I值
    n  = len(data)
    I_first =  n * numpy.std(data)
    return I_first

def fisher_div(data) :
    # 对指定的区间进行二次划分
    n = len(data)
    I = fisher_I(data)
    j = 0
    for i in range(1,int(n)):    # 划分成两个部分，最少是一个值
        if fisher_I(data[:i])+fisher_I(data[i:]) < I:
            I = fisher_I(data[:i])+fisher_I(data[i:])
            j = i    # i表示选择前i个数据
    return I, j




if __name__ == '__main__':
    fileName = 'pre_xun.txt'
    filePath = eachFile(fileName)
    pre_m = open(filePath)
    data_m = numpy.loadtxt(pre_m)
    x, y = data_m.shape
    data_m_t = numpy.zeros((x, y))
    scaler = MinMaxScaler()
    scaler.fit(data_m)
    data_m_t = scaler.transform(data_m)
    # print (data_m_t)
    # D2 = numpy.zeros((y, x - 1, x - 1))  # 反期间
    # D1 = numpy.zeros((y, x))  # 仅去除一个  在旬中不考虑
    D3 = numpy.zeros((y, x))  # 非首尾相连
    writer = pandas.ExcelWriter('fisher_xun2k.xlsx')
    I = numpy.zeros((y,x,x))  # 期间
    for k in range(y):
        for i in range(x):
            # I = numpy.zeros((y, i, i))  # 期间
            D3[k, i] = i * numpy.std(data_m_t[:i, k]) + (12*3 - i) * numpy.std(data_m_t[i:, k])
            for j in range(i,x-1):
                I[k, i, j ] = (i) * numpy.std(data_m_t[:i, k]) + ( j - i ) * numpy.std(data_m_t[i:j, k]) + ( x - j ) * numpy.std(data_m_t[j:, k])
        #df = pandas.DataFrame(I[k, :,:])
        #df.to_excel(writer, '%sk' % (k))
        #writer.save()
                # D2[k,i,j-1] = (12*3-(j-i+1)) * numpy.std ( numpy.append(data_m_t[:i,k],data_m_t[j:,k]) )

    #            for l in range(x):
    #                D1[k, l] = 11 * numpy.std(numpy.delete(data_m_t[:, k], l))
    # print (D2[1,:,:])

    # file = os.getcwd()
    # f = open('%s\data\pretreatment\D.txt'%(file),'w')
    # numpy.savetxt('%s\data\pretreatment\D.txt'%(file),D2[1,:,:])
    # f.close()

