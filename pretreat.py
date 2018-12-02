import numpy



def max_n(data,n):
    l = len(data)
    x = 0
    for i in range(l-n+1):
        x = max(x,numpy.sum(data[i:i+n]))
        #print (x,numpy.sum(data[i:i+n]))
    return x


if __name__ == '__main__':
    fileName = '旬逐日流量.txt'
    pre_m = open(fileName)
    data_m = numpy.loadtxt(pre_m)
    x,y = data_m.shape
    max3 = numpy.zeros((int(x),int(y/11)))
    max1 = numpy.zeros((int(x), int(y / 11)))
    CV = numpy.zeros((int(x), int(y / 11)))
    for i in range(x):
        for j in range(int(y/11)):
            data = (data_m[i,j*11:(j+1)*11])
            data = data[numpy.nonzero(data)]
            max3[i,j] = max_n(data,3)


    output = numpy.zeros((int(x), 4))
    for i in range(x):
        for j in range (4):
            print(max1[i,j]-max(data))

