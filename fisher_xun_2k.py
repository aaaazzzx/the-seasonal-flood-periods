import os
import pandas
import numpy

from sklearn.preprocessing import MinMaxScaler





if __name__ == '__main__':
    fileName =  'I3.txt'    #逐旬综合指标
    pre_m = open(fileName)
    data_m = numpy.loadtxt(pre_m)
    n, = data_m.shape    #长度 36旬
    # print (data_m_t)
    # D = numpy.zeros(())  # 期间
    # D2 = numpy.zeros((n - 1, n - 1))  # 反期间
    # D1 = numpy.zeros((y, x))  # 仅去除一个  在旬中不考虑
    D3 = numpy.zeros((n, n))  # 划分
    for i in range(n-1):
        for j in range(i+1,n):    #至少包含一个数据
            D3[i, j] = (j-i) * numpy.std(data_m[i:j]) + (n - (j-i)) * numpy.std ( numpy.append(data_m[:i],data_m[j:]) )
            print((j-i) , numpy.std(data_m[i:j]) , (n - (j-i)),data_m[:i],data_m[i:j],data_m[j:])
            '''
            j = 18
            if i< j :
                D[k, i, j - 1] = (j - i + 1) * numpy.std(data_m_t[i:j + 1, k])
                D2[k,i,j-1] = (12*3-(j-i+1)) * numpy.std ( numpy.append(data_m_t[:i,k],data_m_t[j:,k]) )

    #            for l in range(x):
    #                D1[k, l] = 11 * numpy.std(numpy.delete(data_m_t[:, k], l))
    # print (D2[1,:,:])
    '''
    file = os.getcwd()
    # f = open('%s\data\pretreatment\D.txt'%(file),'w')
    # numpy.savetxt('%s\data\pretreatment\D.txt'%(file),D2[1,:,:])
    # f.close()
    writer = pandas.ExcelWriter('outputD_xun_2k.xlsx')
    df = pandas.DataFrame(D3)
    df.to_excel(writer, 'Sheet1' )
    writer.save()