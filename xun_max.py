# 用于计算月最大流量所在日期，以求得按旬分期的分期最大值序列

import numpy
import fisher_2k
import pandas
import xlrd
import copy


def list_pre(n,a,b):
    # 将月最值按旬划分不同时段,其中n为原序列，a、b为旬实际划分[9,19][20,25][5,8][26,30][31,36][1,4]
    # 用来保存输出序列
    m  = []
    for [y,c,max] in n :
        if c>=a and c<=b :
            m.append([y,c,max])
    return m

def list_max(n):
    a = n.year.min()
    b = n.year.max()
    result = pandas.DataFrame(columns=['year','xun','data'])
    for i in range(a,b+1):
        m = n[n.year==i]
        new1 = m[m.data==m.data.max()]
        result = pandas.concat([result,new1], axis=0, ignore_index=True)
        # print(new1)
        # print(result)
    return result
    # for i in range(a,b+1):


# 读取逐日流量数据
if __name__ == '__main__':
    fileName = '毛俊日流量表1973-2003.xls'
    file = fisher_2k.eachFile(fileName)
    readbook = xlrd.open_workbook(file)

    #  print(xls_file.sheet_names)
    n = []   # 用来保存各个月最大值所在旬位置，以全年表示[年，旬，流量]
    # 选出月最值所在旬,旬为实际（已+1）
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
            # print(out)
            n.append(out)
    # print(n)
    m1_4 = list_pre(n,1,4)
    m5_8 = list_pre(n,5,8)
    m9_19 = list_pre(n,9,19)
    m20_25 = list_pre(n,20,25)
    m26_30 = list_pre(n,26,30)
    m31_36 = list_pre(n,31,36)

    '''
    m9_25 = list_pre(n,9,25)
    m9_25 = pandas.DataFrame(m9_25,columns=['year','xun','data'])
    #print(m31_36)
    m1_4 = pandas.DataFrame(m1_4,columns=['year','xun','data'])
    #print(m1_4)
    list_max(m1_4)
    l = list_max(m9_25)
    # print(l)
    writer = pandas.ExcelWriter('final_9_25.xlsx')
    l.to_excel(writer)
    writer.save()
    '''

    '''
    '''
    m26_36 = list_pre(n,26,36)
    m1_8 = list_pre(n,1,8)
    m26_36 = pandas.DataFrame(m26_36,columns=['year','xun','data'])
    m1_8 = pandas.DataFrame(m1_8,columns=['year','xun','data'])
    l1 = list_max(m26_36)
    l2 = list_max(m1_8)
    # print(l1)
    writer = pandas.ExcelWriter('final_26_8.xlsx')
    result = pandas.concat([l1, l2], axis=0, ignore_index=True)
    result.to_excel(writer)
    writer.save()


