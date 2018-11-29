import xlrd
import numpy

readbook = xlrd.open_workbook(r'H:\the-seasonal-flood-periods\data\source\毛俊日流量表1973-2003.xls')
Q = numpy.zeros((31, 12, 31))  # 年，月，日
for i in range(1973,2004):    #31 年
    sheet = readbook.sheet_by_name('%s'%(i))  # 名字的方式
    for j in range(12):    #12 月
        for k in range(31):    #31   日
            #print(type(sheet.cell_value(k+2,j+1)))
            if isinstance(sheet.cell_value(k+2,j+1),float):
                Q[i-1973,j,k] = float(sheet.cell_value(k+2,j+1))
            else :
                Q[i - 1973, j, k] = 0
output = numpy.zeros((12*3, 11*31))
for i in range(12*3):    #旬j
    for j in range(31):    #年
        for k in range(10):     #日
            output[i,j*11+k] = Q[j,int(i*3),k+i*10]
            print(j*11+k)
        if i % 3 == 0:
            print (j*11+10)
            #output[i, j*11+11] = Q[j,int(i*3),11+i*10]

    #print  (output[i, :])
