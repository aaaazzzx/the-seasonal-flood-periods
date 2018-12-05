import numpy
import os
import pandas

if __name__ == '__main__':
    fileName = 'Dxun.txt'
    pre_m = open(fileName)
    data_m = numpy.loadtxt(pre_m)     #逐旬逐年的4个指标
    n,m = data_m.shape
    C = numpy.zeros(3)
    c = numpy.zeros(3)
    data = numpy.zeros((3,n,int(m/4)))
    for i in range(3):
        for j in range(n):
            for k in range(int(m/4)):
                data[i,j,k] = data_m[j,k*4+i]
                #print(i,j,k,data[i,j,k])
        C[i] = numpy.std(data[i,:,:],ddof=1)/numpy.mean(data[i,:,:])
    for i in range(3):
        c[i] = C[i]/sum(C)
        #print (c[i])
    file = os.getcwd()
    f = open('%s\data\pretreatment\Guiyi3.txt'%(file),'w')    #前3个指标的权重
    numpy.savetxt('%s\data\pretreatment\Guiyi3.txt'%(file),c)
    f.close()
    data = numpy.zeros((n,int(m/4)))
    for i in range(n):
        for j in range(int(m/4)):
            data[i,j] = numpy.matmul(data_m[i,j*4:(j*4+3)],c.T)
            #print (data_m[i,j*4:(j*4+3)],c.T,data[i,j])
    #print(data.shape)
    f = open('%s\data\pretreatment\旬逐年综合指标.txt'%(file),'w')    #逐旬逐年综合指标
    numpy.savetxt('%s\data\pretreatment\旬逐年综合指标.txt'%(file),data)
    writer = pandas.ExcelWriter('旬逐年综合指标.xlsx')
    df = pandas.DataFrame(data)
    df.to_excel(writer, 'Sheet1')
    writer.save()
    f.close()
    I = numpy.zeros((n))    #逐旬综合指标
    #a = numpy.zeros(int(m/4))
    for i in range(n):
        I[i] = numpy.mean(data[i,:])
        print(I[i])
    f = open('%s\data\pretreatment\I3.txt'%(file),'w')
    numpy.savetxt('%s\data\pretreatment\I3.txt'%(file),I)
    f.close()
    writer = pandas.ExcelWriter('I3.xlsx')
    df = pandas.DataFrame(I)
    df.to_excel(writer, 'Sheet1')
    writer.save()