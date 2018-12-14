# 用于计算月最大流量所在日期，以求得按旬分期的分期最大值序列

import numpy
import fisher_2k
import pandas
import xlrd
import copy


# 读取逐日流量数据
if __name__ == '__main__':
    fileName = '毛俊日流量表1973-2003.xls'
    file = fisher_2k.eachFile(fileName)
    readbook = xlrd.open_workbook(file)

    #  print(xls_file.sheet_names)
    n = []   # 用来保存各个月最大值所在旬位置，以全年表示[年，旬，流量]
    for i in range(1973, 2004):  # 31 年
        sheet = readbook.sheet_by_name('%s' % (i))  # 名字的方式
        for j in range(12):    # 逐月查找
            cell = sheet.col_values(j+1)
            Q = cell[2:31+2]
            Q = list(filter(None, Q))
            Q_max = cell[31+3]
            # print(Q)
            weizhi = Q.index(max(Q))
            if weizhi<=10 :
                weizhi = 1 + j*3
            elif weizhi<=20 :
                weizhi = 2 + j*3
            else:
                weizhi = 3 + j*3
            out = []
            out.append(i)
            out.append(weizhi)
            out.append(Q_max)
            print(out)
            n.append(out)
    print(n)