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
    print (data_m)