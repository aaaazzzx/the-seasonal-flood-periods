import os
import pandas
import numpy

#查找当前文件夹下的指定文件，同时返回文件目录
def eachFile(filename): 
    file = os.getcwd()    
    for root,dirs,files in os.walk(file):
        if filename in files:
            filePath = os.path.join(str(root),str(dirs))
            filePath = filePath[:-2]+filename
    return filePath


def loadDatadet(infile,k):
    f=open(infile,'r')
    sourceInLine=f.readlines()
    dataset=[]
    for line in sourceInLine:
        temp1=line.strip('\n')
        temp2=temp1.split()
        dataset.append(temp2)
    for i in range(0,len(dataset)):
        for j in range(k):
            dataset[i].append(float(dataset[i][j]))
        del(dataset[i][0:k])
    return dataset





if __name__ == '__main__':
    fileName = 'data_m.txt'
    filePath = eachFile(fileName)
    data_m = open(filePath)
    line = data_m.readline()
    infile=loadDatadet(filePath,961)  #961为每行所含数字
    data_m = numpy.array(infile)
    x,y= data_m.shape
    for i in range(x):
        for j in range(int(y/31)):
            data_now = data_m[i,j*31:(j+1)*31]
            data_now = data_now[data_now>0.000001]
            

 

