# 用于洪水分期的模糊集合法
import os
import pandas
import numpy


# 查找当前文件夹下的指定文件，同时返回文件目录
def eachFile(filename):
    file = os.getcwd()
    for root, dirs, files in os.walk(file):
        if filename in files:
            filePath = os.path.join(str(root), str(dirs))
            filePath = filePath[:-2] + filename
    return filePath


def loadDatadet(infile, k):
    f = open(infile, 'r')
    sourceInLine = f.readlines()
    dataset = []
    for line in sourceInLine:
        temp1 = line.strip('\n')
        temp2 = temp1.split()
        dataset.append(temp2)
    for i in range(0, len(dataset)):
        for j in range(k):
            dataset[i].append(float(dataset[i][j]))
        del (dataset[i][0:k])
    return dataset


def List_max(list, n):
    x = len(list)
    y = numpy.zeros(x - n + 1)
    for i in range(x - n + 1):
        y[i] = numpy.sum(list[i:i + n])
    y = numpy.max(y)
    return y


if __name__ == '__main__':
    fileName = r'旬逐日流量.txt'
    pre_m = open(fileName)
    data_m = numpy.loadtxt(pre_m)
    x, y = data_m.shape
    print (x,y)    #36,341=11*31
    data_pr = numpy.zeros((x, 4*int(y / 11)))
    xun_mean = numpy.zeros((x,31))
    for i in range(x):
        for j in range(int(y / 11)):
            data_now = data_m[i, j * 11:(j + 1) * 11]
            data_now = data_now[data_now > 0]
            data_pr[i, j*4+0] = numpy.mean(data_now)
            xun_mean[i,j] = numpy.mean(data_now)
            data_pr[i, j*4+1] = List_max(data_now, 1)
            data_pr[i, j*4+2] = List_max(data_now, 3)
            data_pr[i, j*4+3] = numpy.std(data_now, ddof=1) / data_pr[i, j*4+0]

    # print(xun_1)
    # print(numpy.mean(xun_1))

    # file = os.getcwd()
    # f = open('%s\data\pretreatment\xun.txt' % (file), 'w')
    # numpy.savetxt('%s\data\pretreatment\xun.txt' % (file), data_pr)
    # f.close()



    # 设定划分依据，此处采用旬均值

    xun_pj = numpy.mean(xun_mean)
    print(xun_pj)

    # print(numpy.mean(data_m))
    # print(numpy.mean(data_pr[:,0::4]))
    # print(data_pr[0,0::4])
    # print(numpy.mean(xun_mean))


    #对比
    n = numpy.zeros((36,31))
    p = numpy.zeros(36)
    for i in range(36):
        for j in range(31):
            if xun_mean[i,j] >= xun_pj :
                n[i,j] = 1
        p[i] = numpy.mean(n[i,:])
    print(p)

    writer = pandas.ExcelWriter('mohu_xun.xlsx')  # P
    df = pandas.DataFrame(p)
    df.to_excel(writer, 'Sheet1' )
    writer.save()