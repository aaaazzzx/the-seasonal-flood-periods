import copy
import numpy
import pandas
data = [1,2,3,4,5,6]
b = [[1,2,3],[4,5,numpy.nan]]
b = pandas.DataFrame(b,columns=['year','aaa','ccc'])
a = [[1,2,4]]
a = pandas.DataFrame(a,columns=['year','aaa','ccc'])
res = pandas.DataFrame(columns=['year','aaa','ccc'])
res = pandas.concat([res,b],axis=0,ignore_index=True)
print(res)


b.loc['new'] = '3'
# print(b)
#a = [[] for _ in range(3)]
#print(a)
'''
df=pandas.DataFrame({'key1':['a','a','b','b','a'],'key2':['one','two','one','two','one'],'data1':numpy.random.randn(5),'data2':numpy.random.randn(5)})
print(df)
grouped1 = df.groupby('key1')
print(grouped1)'''