import xlrd
import numpy
import pandas
import os
from pre_xun import List_max

# 月数据处理
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
                # 读取完毕
output = numpy.zeros((12, 31*31))
writer = pandas.ExcelWriter(r'月逐日流量.xlsx')
for i in range(12):    #月
    for j in range(31):    #年
        for k in range(31):     #日
            output[i,j*31+k] = Q[j,i,k]
            # print(j,int(i/3),k+(i%3)*10)
            # 重新排列
df = pandas.DataFrame(output)
df.to_excel(writer, 'sheet1' )
writer.save()
f = open(r'月逐日流量.txt','w')
numpy.savetxt(r'月逐日流量.txt',output)
f.close()

# 数据分析，提取相关系数
data_m = output
x, y = data_m.shape
print(x, y)
data_pr = numpy.zeros((x, 4 * int(y / 11)))

for i in range(x):
    for j in range(int(y / 11)):
        data_now = data_m[i, j * 11:(j + 1) * 11]
        data_now = data_now[data_now > 0]
        data_pr[i, j * 4 + 0] = numpy.mean(data_now)
        data_pr[i, j * 4 + 1] = List_max(data_now, 1)
        data_pr[i, j * 4 + 2] = List_max(data_now, 3)
        data_pr[i, j * 4 + 3] = List_max(data_now, 7)

file = os.getcwd()

f = open('%s\data\pretreatment\Dyue.txt' % (file), 'w')
numpy.savetxt('%s\data\pretreatment\Dyue.txt' % (file), data_pr)    #逐年的4个指标
f.close()

writer = pandas.ExcelWriter('yue.xlsx')    #逐年的4个指标
df = pandas.DataFrame(data_pr)
df.to_excel(writer, 'Sheet%s' % (i))
writer.save()