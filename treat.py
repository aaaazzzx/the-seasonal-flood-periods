import os
import pandas
import numpy

from sklearn.preprocessing import MinMaxScaler


def eachFile(filename): 
    file = os.getcwd()
    for root,dirs,files in os.walk(file):
        if filename in files:
            filePath = os.path.join(str(root),str(dirs))
            filePath = filePath[:-2]+filename
    return filePath



if __name__ == '__main__':
    fileName = 'pre_m.txt'
    filePath = eachFile(fileName)
    pre_m = open(filePath)
    data_m = numpy.loadtxt(pre_m)
    x,y= data_m.shape
    data_m_t = numpy.zeros((x,y))
    scaler = MinMaxScaler()
    scaler.fit(data_m)
    data_m_t=scaler.transform(data_m)
    # print (data_m_t)
    D = numpy.zeros((y,x-1,x-1))
    D2 = numpy.zeros((y,x-1,x-1))
    for k in range(y):
        for i in range(x-1):
            for j in range(i+1,x):
                print (i,j)
                print (data_m_t[i:j+1,k])
                D[k,i,j-1] = (j-i+1)*numpy.std(data_m_t[i:j+1,k])
                D2[k,i,j-1] = (12-(j-i+1)) * numpy.std ( numpy.append(data_m_t[:i,k],data_m_t[j:,k]) )
    print (D2[1,:,:])
    
    file = os.getcwd()
    f = open('%s\data\pretreatment\D2.txt'%(file),'w')
    numpy.savetxt('%s\data\pretreatment\D2.txt'%(file),D2[1,:,:])
    writer = pandas.ExcelWriter('output.xlsx')
    for i in range(y):
        df = pandas.DataFrame(D2[i,:,:])
        df.to_excel(writer,'Sheet%s'%(i))
        writer.save()
    f.close()
