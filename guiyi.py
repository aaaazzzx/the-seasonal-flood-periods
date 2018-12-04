import numpy
import os

if __name__ == '__main__':
    fileName = 'Dxun.txt'
    pre_m = open(fileName)
    data = numpy.loadtxt(pre_m)
    n,m = data.shape
    C = numpy.zeros(3)
    c = numpy.zeros(3)
    for i in range(3):
        C[i] = numpy.std(data[:,i],ddof=1)/numpy.mean(data[:,i])
    for i in range(3):
        c[i] = C[i]/sum(C)
        print (c[i])
    file = os.getcwd()
    f = open('%s\data\pretreatment\Guiyi3.txt'%(file),'w')
    numpy.savetxt('%s\data\pretreatment\Guiyi3.txt'%(file),c)
    f.close()