import numpy
import os
import pandas

if __name__ == '__main__':
    file = os.getcwd()
    f = open('%s\data\pretreatment\Guiyi3.txt'%(file))
    C = numpy.loadtxt(f)
    fileName = 'Dxun.txt'
    pre_m = open(fileName)
    data = numpy.loadtxt(pre_m)
    data = numpy.delete(data,-1,axis=1)    #去掉最后一列
    n,m = data.shape
    I = numpy.zeros(n)
    #for i in range(n):
    I = numpy.matmul(data,C)
    #print(C,data)
    file = os.getcwd()
    f = open('%s\data\pretreatment\I3.txt'%(file),'w')
    numpy.savetxt('%s\data\pretreatment\I3.txt'%(file),I.T)
    f.close()
    writer = pandas.ExcelWriter('I3.xlsx')
    df = pandas.DataFrame(I.T)
    df.to_excel(writer, 'Sheet1' )
    writer.save()